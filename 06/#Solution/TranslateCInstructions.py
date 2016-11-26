import re

regex = "([AMD0]*)(=?)([AMD+-1!0&|]*)(;?)(.*)"

rg = re.compile(regex, re.IGNORECASE | re.DOTALL)
compADict = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100',
			 'A': '110000', '!D': '001101', '!A': '110001',
			 '-D': '001111', '-A': '110011', 'D+1': '011111',
			 'A+1': '110111', 'D-1': '001110', 'A-1': '110010',
			 'D+A': '000010', 'D-A': '010011', 'A-D': '000111',
			 'D&A': '000000', 'D|A': '010101'}

compMDict = {'M': '110000', '!M': '110001',
			 '-M': '110011',
			 'M+1': '110111', 'M-1': '110010',
			 'D+M': '000010', 'D-M': '010011', 'M-D': '000111',
			 'D&M': '000000', 'D|M': '010101'}

destDict = {'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
			'AM': '101', 'AD': '110', 'AMD': '111'}

jumpDict = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
			'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}


def TranslateCIns(asmList):
	newList = []
	for line in asmList:
		match = rg.search(line)
		if match:
			instruction = '111'
			if (line.startswith('0') and line[1].isdigit()):
				newList.append(line)
				continue
			elif (match.group(2)):
				if (match.group(3) in compADict.keys()):
					instruction += '0'
					instruction += compADict[match.group(3)]
				elif (match.group(3) in compMDict.keys()):
					instruction += '1'
					instruction += compMDict[match.group(3)]
				destEntry = destDict[match.group(1)]
				instruction += destEntry
			else:
				if (match.group(1) in compADict.keys()):
					instruction += '0'
					instruction += compADict[match.group(1)]
				elif (match.group(1) in compMDict.keys()):
					instruction += '1'
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
