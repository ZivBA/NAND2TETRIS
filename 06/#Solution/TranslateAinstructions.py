import re


re1 = '(@)'  # Any Single Character 1
re2 = '(.*)'  # Integer Number 1

rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)


def TranslateAIns(asmList, labelsDict):
    newList = []
    addressDict = {}
    for line in asmList:
        match = rg.search(line)
        if match and match.group(1):
            if (match.group(2) in labelsDict.keys()):
                newList.append(
                    format(int(labelsDict[match.group(2)]), '016b'))
            else:
                try:
                    newList.append(format(int(match.group(2)), '016b'))
                except(Exception):
                    address, addressDict = AddKeyToDict(match.group(2), addressDict)
                    newList.append(format(int(address), '016b'))

        else:
            newList.append(line)
    return newList


def AddKeyToDict(key, addressDict):
    for i in range(16, 16384):
        if i not in addressDict.values():
            addressDict[key] = i
            return i, addressDict
