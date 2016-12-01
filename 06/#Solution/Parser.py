import os
import re

COMMENT_LINE_PATTERN = "^\s*[\/\/]+.*$"  # RE to capture comment line
INLINE_COMMENT_PATTERN = "^(?:\s*)([^\s]*?)(?:\s*)(?:\/\/.*)?$"  # RE to catpure inline comment


RE_COMMENT_LINE = re.compile(COMMENT_LINE_PATTERN)
RE_INLINE_COMMENT = re.compile(INLINE_COMMENT_PATTERN)

EMTPY_LINE = ""  # New line character



def PreprocessFile(LINES):
    FILE_CONTENT = []

    for line in LINES:
        if (line == EMTPY_LINE):  # If an empty line --> Skip it.
            continue
        elif (RE_COMMENT_LINE.match(line)):  # If comment line --> Skip it
            continue
        regexMatcher = RE_INLINE_COMMENT.search(line)
        if (regexMatcher):
            regexContent = regexMatcher.group(1)
            FILE_CONTENT.append(regexContent)

    return FILE_CONTENT
