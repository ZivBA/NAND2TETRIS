import re
labelRegex = '\\((.*)\\)'
rg = re.compile(labelRegex, re.IGNORECASE | re.DOTALL)
labelsDict = {}
newFile = []


def BuildSymbolTable(asmFile):
    linesRemoved = -1
    for idx, line in enumerate(asmFile):
        match = rg.search(line)
        if match:
            label = match.group(1)
            labelsDict[label] = idx - linesRemoved
            linesRemoved += 1
        else:
            newFile.append(line)
    return labelsDict, newFile
