import re

CONTENT_EXTRACT_PATTERN = "^(.*?)(\/\/.+)?$"  # RE to capture the content and ignore the reset
RE_CONTENT_EXTRACT = re.compile(CONTENT_EXTRACT_PATTERN)
EMTPY_LINE = ""  # Empty line


def PreprocessFile(LINES):
    """
    This function extracts the actual relevant content. Meaning it completely ignores Comments, In-line comments
    and empty lines.
    :param LINES: The content of the '.asm' file after being processed by '.splitlines()' function
    :return: The content of the file in plain Hack syntax
    """
    FILE_CONTENT = []

    for line in LINES:
        # Extracting the content, replacing all spaces with "" to promote cleanliness of the Hack syntax
        newLine = RE_CONTENT_EXTRACT.match(line).group(1).replace(" ", "")
        if (newLine == EMTPY_LINE):  # If an empty line --> Skip it.
            continue
        FILE_CONTENT.append(newLine)  # Else, add the content that was extracted.
    return FILE_CONTENT
