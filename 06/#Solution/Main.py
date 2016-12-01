import Parser
import BuildSymbolTable
import TranslateAinstructions
import TranslateCInstructions
import sys
import os

INPUT_FILE_TYPE = ".asm"
OUTPUT_FILE_TYPE = ".hack"

BAD_NUMBER_OF_INPUTS_ERROR = "Bad usage! You must provide a path to either: " \
                             "\n1) Path to an '.asm' file " \
                             "\n2) Path to a directory containing '.asm' files"


def getFileName(pathToFile):
    """
    Function that is used to extract the loaded '.asm' file name
    :param pathToFile: Absolute path to the given '.asm' file
    :return: Path - The absolute path to the directory of the '.asm' file.
             fileName - The file name without extension.
    """
    path, fileName = os.path.split(os.path.abspath(pathToFile))
    fileName = fileName.split(".")
    return path, fileName[0]


def writeToFile(CONTENT, PATH, FILE_NAME):
    """
	Writes the Hack Assembler output into a file
    :param CONTENT: The content to output
    :param PATH: The absolute path
    :param FILE_NAME: The file name
    """
    with open(PATH + os.sep + FILE_NAME + OUTPUT_FILE_TYPE, mode="w+") as f:
        for k in range(len(CONTENT)):
            f.write(CONTENT[k])
            if (k < len(CONTENT) - 1):  # Avoiding empty line at EOF
                f.write("\n")


def translateToHack(filePath):
    """
    Translates '.asm' files to Hack
    :param filePath: Given path to an '.asm' file
    """
    with open(filePath, mode="r") as f:
        CONTENT = Parser.PreprocessFile(f.read().splitlines())

    addrDict, newList = BuildSymbolTable.BuildSymbolTable(CONTENT)
    newList = TranslateAinstructions.TranslateAIns(newList, addrDict)
    finalOutput = TranslateCInstructions.TranslateCIns(newList)
    outputPath, outputName = getFileName(filePath)
    writeToFile(finalOutput, outputPath, outputName)


def driver(argv):
    """
    Main driver function. Iterates over '.asm' files in a given directory and translates it to Hack.
    :param argv: The program arguments.
    """
    if (len(argv) == 1):
        sys.exit(BAD_NUMBER_OF_INPUTS_ERROR)
    DIR_PATH = argv[1]
    if (DIR_PATH.endswith(INPUT_FILE_TYPE)):  # If given path is to an '.asm' file
        translateToHack(DIR_PATH)
    else:  # Given path is to a directory
        for fileName in os.listdir(DIR_PATH):
            if fileName.endswith(INPUT_FILE_TYPE):
                translateToHack(DIR_PATH + os.sep + fileName)
            else:
                continue




# Run main function:
driver(sys.argv)
