import Parser
import sys


def main(argv):
	print("Number of args: " + str(len(argv)))
	print("The arguments: " + str(argv))
	FILE = open(argv[1], mode="r+")
	Parser.RemoveWhiteSpaces(FILE)
	FILE.close()


main(sys.argv)