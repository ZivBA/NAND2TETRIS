import re


re1 = '(@)'  # Any Single Character 1
re2 = '(.*)'  # Integer Number 1

rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)


def TranslateAIns(asmList, labelsDict):
    """
    Main translation unit for A instructions. goes line by line and searches for an @ symbol. if found
    it tries to match the string that follows it to the labels dictionary it received as parameter.
    if a label is matched, it's value from the dictionary is converted to binary form and the line is replaced.
    if no loabel is found, an address integer is assumed as the same follows.
    :param asmList:     list of ASM lines to proess, cleaned by parser from comments and spaces.
    :param labelsDict:  a dictionary of possible labels created by the SymbolTable builder in a previous step.
    :return:            a new list of translated A instructions and unchanged C instructions for further processing.
    """
    newList = []
    addressDict = {}
    for line in asmList:
        match = rg.search(line)
        if match and match.group(1):
            if (match.group(2) in labelsDict.keys()):
                newList.append(
                    format(int(labelsDict[match.group(2)]), '016b'))
            elif (match.group(2) in addressDict.keys()):
                newList.append(
                    format(int(addressDict[match.group(2)]), '016b'))

            else:
                try:
                    newList.append(format(int(match.group(2)), '016b'))
                except(Exception):
                    address, addressDict = AddKeyToDict(
                        match.group(2), addressDict)
                    newList.append(format(int(address), '016b'))

        else:
            newList.append(line)
    return newList


def AddKeyToDict(key, addressDict):
    """
    helper method to add a key to the address dictionary.
    it maintains the convention that only certain addresses are applicable, and pushes new addresses where an available
    space exists.
    :param key:         key to insert
    :param addressDict: preexisting address dictionary.
    :return: the index assigned and the modified dictionary.
    """
    for i in range(16, 16384):
        if i not in addressDict.values():
            addressDict[key] = i
            return i, addressDict
