import re
labelRegex = '\\((.*)\\)'
rg = re.compile(labelRegex, re.IGNORECASE | re.DOTALL)
labelsDict = {'R0': '0', 'R1': '1', 'R2': '2',
              'R3': '3', 'R4': '4', 'R5': '5',
              'R6': '6', 'R7': '7', 'R8': '8',
              'R9': '9', 'R10': '10', 'R11': '11',
              'R12': '12', 'R13': '13', 'R14': '14',
              'R15': '15', 'SP': '0', 'LCL': '1',
              'ARG': '2', 'THIS': '3', 'THAT': '4',
              'SCREEN': '16384', 'KBD': '24576'}
newFile = []


def BuildSymbolTable(asmFile):
    linesRemoved = 0
    for idx, line in enumerate(asmFile):
        match = rg.search(line)
        if match:
            label = match.group(1)
            labelsDict[label] = idx - linesRemoved
            linesRemoved += 1
        else:
            newFile.append(line)
    return labelsDict, newFile
