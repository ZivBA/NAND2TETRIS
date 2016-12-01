import re

regex = "([AMD0]*)(=?)([AMD+-1!0&><|]*)(;?)(.*)"

rg = re.compile(regex, re.IGNORECASE | re.DOTALL)
compADict = {'0': '1110101010', '1': '1110111111', '-1': '1110111010',
             'D': '1110001100', 'A': '1110110000', '!D': '1110001101',
             '!A': '1110110001', '-D': '1110001111', '-A': '1110110011',
             'D+1': '1110011111', 'A+1': '1110110111', 'D-1': '1110001110',
             'A-1': '1110110010', 'D+A': '1110000010', 'D-A': '1110010011',
             'A-D': '1110000111', 'D&A': '1110000000', 'D|A': '1110010101',
             'D<<': '1010110000', 'D>>': '1010010000', 'A>>': '1010000000',
             'A<<': '1010100000'}

compMDict = {'M': '1111110000', '!M': '1111110001',
             '-M': '1111110011', 'M+1': '1111110111', 'M-1': '1111110010',
             'D+M': '1111000010', 'D-M': '1111010011', 'M-D': '1111000111',
             'D&M': '1111000000', 'D|M': '1111010101',
             'M<<': '1011100000', 'M>>': '1011000000'}

destDict = {'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
            'AM': '101', 'AD': '110', 'AMD': '111'}

jumpDict = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
            'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}


def TranslateCIns(asmList):
    newList = []
    for line in asmList:
        match = rg.search(line)
        instruction = ''
        if match:
            if (line.startswith('0') and line[1].isdigit()):
                newList.append(line)
                continue
            elif (match.group(2)):
                if (match.group(3) in compADict.keys()):
                    # instruction += '0'
                    instruction += compADict[match.group(3)]
                elif (match.group(3) in compMDict.keys()):
                    # instruction += '1'
                    instruction += compMDict[match.group(3)]
                destEntry = destDict[match.group(1)]
                instruction += destEntry
            else:
                if (match.group(1) in compADict.keys()):
                    # instruction += '0'
                    instruction += compADict[match.group(1)]
                elif (match.group(1) in compMDict.keys()):
                    # instruction += '1'
                    instruction += compMDict[match.group(1)]
                instruction += destDict['null']
            if (match.group(4)):
                jumpEntry = jumpDict[match.group(5)]
                instruction += jumpEntry
            else:
                instruction += jumpDict['null']
            newList.append(instruction)

        else:
            newList.append(line)
    return newList
