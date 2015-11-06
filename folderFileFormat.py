#! python3

# folderFileFormat.py
# Takes a list from the clipboard, looks for numbers in the list to
# signify that a folder has started and creates a sequential folder-file
# prefix for the remaining list items until the next folder.

# Output example:
# 1 First folder/chapter
# 01-01 First folder file one
# 01-02 First folder file two
# 01-03 First folder file three
# 2 Second folder/chapter
# 02-01 Second folder file one
# 02-02 Second folder file two
# 02-03 Second folder file three


# Note to self regarding regular expressions:
# https://docs.python.org/3/howto/regex.html
# Also, your parents are very disappointed in you for not using re and
# you should call them more often.


# pyperclip is needed to access copied text from the clipboard.
import pyperclip


# Grabs text from the clipboard.
text = pyperclip.paste()


# Makes text into a list, separated by returns by default
def list_maker(text, separator = "\n"):
    return text.split(separator)


# Pads single digit numbers with a 0 (3 becomes 03, 11 stays 11).  
def int_to_str_pad(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


# Adds "xx-yy " format before each file name in the list.  Chapters are
# not renamed, but numbers are taken from chapter names.
def chapter_format(text, separator = "\n", chapterMax = 30, 
                  chapterMin = 0):
    # Make a list from copied text.
    textList = list_maker(text, separator)
    # Set counter for chapter and section.
    chapter = 0
    section = 1
    # Search current string for a chapter number and update if found.
    # Add xx-yy format if not and repeat.
    for i in range(len(textList)):
        # format is used to break out of an ugly set of for/if.
        # We all realize this is a hobo work around.
        format = True
        # Search for a chapter number.  If found, set chapter, reset 
        # section, and strip whitespace that somehow sneaks in at the 
        # end.
        # Search counts down from chapterMax to chapterMin, and sets
        # the chapter to the highest number it finds (20 instead of 2).
        for countdown in range(chapterMax, chapterMin - 1, -1):
            if str(countdown) in textList[i]:
                chapter = countdown
                section = 1
                textList[i] = textList[i].strip()
                # Flag that a chapter was found, and skip section format
                format = False
                break
        # If format is True, chapter numbers were not found in the 
        # string and we add increasing section numbers to each file 
        # name.
        if format == True:
            # Convert numbers to strings, and add padding to single
            # digit numbers.
            chapterStr = int_to_str_pad(chapter)
            sectionStr = int_to_str_pad(section)
            # Filename becomes xx-yy Filename
            textList[i] = (chapterStr + "-" + sectionStr + " " +\
                textList[i]).strip()
            section += 1
    return textList


# Demo
for i in chapter_format(text):
    print(i)