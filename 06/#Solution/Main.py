import Parser
import sys


def main(argv):
	FILE = open(argv[1], mode="r")
	CONTENT = Parser.PreprocessFile(FILE)
	FILE.close()
	PrintContent(CONTENT)

def PrintContent(CONTENT):
	for x in CONTENT:
		print(x)


main(sys.argv)