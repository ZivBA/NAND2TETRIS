import re

COMMENT_LINE_PATTERN = "^\s*[\/\/]+.*$"  # RE to capture comment line
INLINE_COMMENT_PATTERN = "^.*(\/\/.*)\s*$"  # RE to catpure inline comment

RE_COMMENT_LINE = re.compile(COMMENT_LINE_PATTERN)
RE_INLINE_COMMENT = re.compile(INLINE_COMMENT_PATTERN)

NEW_LINE = "\n"  # New line character



FILE_CONTENT = []

def RemoveWhiteSpaces(file):
	for line in file:
		if (line == "\n"):  # If an empty line, just skip it...
			continue
		elif (False):
			continue
		FILE_CONTENT.append(line)

	print(str(FILE_CONTENT))
