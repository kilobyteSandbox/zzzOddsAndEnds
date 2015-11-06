#! python3

# folderFileFormat.py
# Takes a list from the clipboard, looks for numbers in the list to
# signify that a folder has started and creates a folder-file prefix for
# remaining list items until the next folder.

# Example:
# 1 First folder
# 01-01 First folder file one
# 01-02 First folder file two
# 01-03 First folder file three
# 2 Second folder
# 02-01 Second folder file one
# 02-02 Second folder file two
# 02-03 Second folder file three


# self note regarding regular expressions:
# https://docs.python.org/3/howto/regex.html

import pyperclip


text = pyperclip.paste()


def listMaker(text, separator = "\n"):
    return text.split(separator)


def intToStrPad(number):
    if number < 10:
        return "0" + str(number)
    else:
        return + str(number)


def chapterFormat(text, separator = "\n", chapterMax = 30, 
                  chapterMin = 0):
    textList = listMaker(text, separator)
    counter = 0
    chapter = 0
    section = 1
    for i in textList:
        format = True
        # Search for a chapter number.  Set chapter and reset section if
        # found.
        # There are many clean ways of doing a search using import re, 
        # but these are uncivilzed times which call for uncivilized 
        # searches.
        # This counts down from chapterMax to chapterMin, and sets
        # the chapter to the highest number it finds (20 instead of 2).
        for countdown in range(chapterMax, chapterMin - 1, -1):
            if str(countdown) in i:
                chapter = countdown
                section = 1
                format = False
        if format == True:
            chapterStr = intToStrPad(chapter)
            sectionStr = intToStrPad(section)
            textList[counter] = chapterStr + "-" + sectionStr + " " +\
                textList[counter]
            section += 1
        counter += 1
    return textList


# Demo
for i in chapterFormat(text):
    print(i)