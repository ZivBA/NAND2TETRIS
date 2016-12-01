import Parser
import BuildSymbolTable
import TranslateAinstructions
import TranslateCInstructions
import sys
import os

FILE_TYPE = ".hack"


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
    with open(PATH + os.sep + FILE_NAME + FILE_TYPE, mode="w+") as f:
        for k in range(len(CONTENT)):
            f.write(CONTENT[k])
            if (k < len(CONTENT) - 1):  # Avoiding empty line at EOF
                f.write("\n")


def driver(argv):
    """
    Main driver function. Loads the given '.asm' file, pre-processes it and translating to Hack
    :param argv: The program arguments.
    """
    with open(argv[1], mode="r") as f:
        CONTENT = Parser.PreprocessFile(f.read().splitlines())

    addrDict, newList = BuildSymbolTable.BuildSymbolTable(CONTENT)

    newList = TranslateAinstructions.TranslateAIns(newList, addrDict)

    finalOutput = TranslateCInstructions.TranslateCIns(newList)

    outputPath, outputName = getFileName(argv[1])
    writeToFile(finalOutput, outputPath, outputName)


# Run main function:
driver(sys.argv)
