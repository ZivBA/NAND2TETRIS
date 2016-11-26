import re


re1 = '(@)'  # Any Single Character 1
re2 = '(\d+)'  # Integer Number 1

rg = re.compile(re1 + re2, re.IGNORECASE | re.DOTALL)


def TranslateAIns(asmList):
    newList = []
    for line in asmList:
        match = rg.search(line)
        if match:
            newList.append(format(int(match.group(2)),'016b'))
        else:
            newList.append(line)
    return newList
