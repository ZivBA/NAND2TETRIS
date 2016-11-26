import re

COMMENT_LINE_PATTERN = "^\s*[\/\/]+.*$"  # RE to capture comment line
INLINE_COMMENT_PATTERN = "^(\s*)(.*?)(\s*\/\/.*)?$"  # RE to catpure inline comment

RE_COMMENT_LINE = re.compile(COMMENT_LINE_PATTERN)
RE_INLINE_COMMENT = re.compile(INLINE_COMMENT_PATTERN)

NEW_LINE = "\n"  # New line character



FILE_CONTENT = []

def PreprocessFile(file):
	for line in file:
		if (line == "\n"):  # If an empty line --> Skip it.
			continue
		elif (RE_COMMENT_LINE.match(line)):  # If comment line --> Skip it
			continue
		m2 = RE_INLINE_COMMENT.search(line)
		if (m2):
			FILE_CONTENT.append(m2.group(2))

	return FILE_CONTENT
