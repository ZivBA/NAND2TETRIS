import os
import re

#COMMENT_LINE_PATTERN = "^\s*[\/\/]+.*$"  # RE to capture comment line
#INLINE_COMMENT_PATTERN = "^(?:\s*)([^\s]*?)(?:\s*)(?:\/\/.*)?$"  # RE to catpure inline comment
INLINE_COMMENT_PATTERN = "^(.*?)(\/\/.+)?$"  # RE to catpure inline comment


#RE_COMMENT_LINE = re.compile(COMMENT_LINE_PATTERN)
RE_INLINE_COMMENT = re.compile(INLINE_COMMENT_PATTERN)

EMTPY_LINE = ""  # New line character



def PreprocessFile(LINES):
    FILE_CONTENT = []

    for line in LINES:
        newLine = RE_INLINE_COMMENT.match(line).group(1).replace(" ", "")
        if (newLine == EMTPY_LINE):  # If an empty line --> Skip it.
            continue
        FILE_CONTENT.append(newLine)

    return FILE_CONTENT
