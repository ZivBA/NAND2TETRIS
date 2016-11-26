import re


re1 = '(@)'  # Any Single Character 1
re2 = '(.*)'  # Integer Number 1

rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)


def TranslateAIns(asmList, addressDict):
    if (not addressDict):
        addressDict = {'null': 'null'}
    newList = []
    for line in asmList:
        match = rg.search(line)
        if match.group(1):
            address = addressDict[match.group(2)]
            if (address):
                newList.append(format(int(address), '016b'))
            else:
                newList.append(format(int(match.group(2)), '016b'))
        else:
            newList.append(line)
    return newList
