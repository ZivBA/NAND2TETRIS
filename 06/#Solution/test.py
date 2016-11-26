from BuildSymbolTable import BuildSymbolTable
from TranslateAinstructions import TranslateAIns
import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

labelDict, newFile = BuildSymbolTable(lines)
for line in newFile:
    print line

for key, value in labelDict.items():
    print("Label:", key, "Value: ", value)

newFile = TranslateAIns(newFile)
for line in newFile:
    print line
