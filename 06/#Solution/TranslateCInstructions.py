import re

# regex to split an instruction string into 5 groups:
# CG1 is the destination address or COMP if no address, CG2 is the '=' operator, if exists.
# CG3 is the comp instruction (mandatory if dest exists), CG4 is the jump operator, if exists.
# final group CG5 is the jump condition, if exists.
regex = "([AMD0]*)(=?)([AMD+-1!0&><|]*)(;?)(.*)"

rg = re.compile(regex, re.IGNORECASE | re.DOTALL)
# dictionary matching each A computation instruction to it's binary representation.
compADict = {'0': '1110101010', '1': '1110111111', '-1': '1110111010',
             'D': '1110001100', 'A': '1110110000', '!D': '1110001101',
             '!A': '1110110001', '-D': '1110001111', '-A': '1110110011',
             'D+1': '1110011111', 'A+1': '1110110111', 'D-1': '1110001110',
             'A-1': '1110110010', 'D+A': '1110000010', 'D-A': '1110010011',
             'A-D': '1110000111', 'D&A': '1110000000', 'D|A': '1110010101',
             'D<<': '1010110000', 'D>>': '1010010000', 'A>>': '1010000000',
             'A<<': '1010100000'}
# dictionary matching each M computation instruction to it's binary representation
compMDict = {'M': '1111110000', '!M': '1111110001',
             '-M': '1111110011', 'M+1': '1111110111', 'M-1': '1111110010',
             'D+M': '1111000010', 'D-M': '1111010011', 'M-D': '1111000111',
             'D&M': '1111000000', 'D|M': '1111010101',
             'M<<': '1011100000', 'M>>': '1011000000'}

# dictionary matching each destination to its binary representation
destDict = {'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
            'AM': '101', 'AD': '110', 'AMD': '111'}

# dictionary matching each jump condition to its binary representation
jumpDict = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011',
            'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}

def TranslateCIns(asmList):
    """
    Main translation unit for C instructions.
    basically checks if an instruction is A - "starts with 0" then it doesnt parse it.
    otherwise it checks for the existance of the "?" and "=" operators to see if a
    jump condition or destination exists, then converts them to their respected binary strings.
    it concatenates the parts of the binary string to create the full binary instruction.
    :param asmList: the list of "clean" instructions to be processed.
    :return: a new list in which each C instruction written in HACK is replaced with a binary equivalent
    """
    newList = []
    for line in asmList:
        match = rg.search(line)
        instruction = ''                                        # start an empty new instruction string.
        if match:
            if (line.startswith('0') and line[1].isdigit()):    # if A inst, skip.
                newList.append(line)
                continue
            elif (match.group(2)):                              # if an "=" op exists, look for computation in CG3
                if (match.group(3) in compADict.keys()):
                    instruction += compADict[match.group(3)]
                elif (match.group(3) in compMDict.keys()):
                    instruction += compMDict[match.group(3)]
                destEntry = destDict[match.group(1)]
                instruction += destEntry
            else:                                               # if no "=" op exists, look for computation in CG1
                if (match.group(1) in compADict.keys()):
                    instruction += compADict[match.group(1)]
                elif (match.group(1) in compMDict.keys()):
                    instruction += compMDict[match.group(1)]
                instruction += destDict['null']                 # and add the "no destination" bits
            if (match.group(4)):                                # if a jump condition exists, find the value of CG5 in
                jumpEntry = jumpDict[match.group(5)]            # the dictionary and add to instruction.
                instruction += jumpEntry
            else:
                instruction += jumpDict['null']                 # otherwise add "no jump" bits.
            newList.append(instruction)

        else:
            raise RuntimeError('something slipped through the cracks')  # should never happen, but must note it.
    return newList
