#! python3

# testCharacters.py
# Test character resource.  This will copy test characters to your 
# clipboard.

# Batch file:
# @py.exe C:\ABSOLUTE_PATH\testCharacters.py %*
# @pause
# or
# @timeout 2

# Example:  Running "chars single" will copy single characters to your
# clipboard.


import sys
import pyperclip


characters = {"single" : "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI" +\
                         "JKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrs" +\
                         "tuvwxyz{|}~",
            "double" : "０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ" +\
                         "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗ",
            "symbol" : "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijk" +\
                       "lmnopqrstuvwxyz{|}~@€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›" +\
                       "œžŸ ¡¢£¤¥¦§¨©ª«¬" }


testType = sys.argv[1]


if testType in characters:
    pyperclip.copy(characters[testType])
    print(testType + " characters copied to clipboard.")
else:
    print("================")
    print("= COPY FAILED! =")
    print("================")
    print(" ")
    print("There is no listing for " + testType + ". Please try again.")