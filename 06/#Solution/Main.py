import Parser, BuildSymbolTable, TranslateAinstructions, TranslateCInstructions
import sys, os

FILE_TYPE = ".hack"

def getFileName(pathToFile):
	path, fileName = os.path.split(pathToFile)
	fileName = fileName.split(".")
	return path, fileName[0]

def PrintContent(CONTENT):
	for x in CONTENT:
		print(x)

def writeToFile(CONTENT, PATH, FILE_NAME):
	"""

	:param CONTENT:
	:param PATH:
	:param FILE_NAME:
	:return:
	"""
	with open(PATH + os.sep + FILE_NAME + FILE_TYPE, mode="w+") as f:
		for k in range(len(CONTENT)):
			f.write(CONTENT[k])
			if (k < len(CONTENT) - 1):  # Avoiding empty line at EOF
				f.write("\n")

def main(argv):
	with open(argv[1], mode="r") as f:
		CONTENT = Parser.PreprocessFile(f)

	addrDict, newList = BuildSymbolTable.BuildSymbolTable(CONTENT)

	newList = TranslateAinstructions.TranslateAIns(newList, addrDict)

	finalOutput = TranslateCInstructions.TranslateCIns(newList)

	outputPath, outputName = getFileName(argv[1])
	writeToFile(finalOutput, outputPath, outputName)

# Run main function:
main(sys.argv)