# randomString.py

# Creates a random string.  User can set length and types of characters
# to be used.  Great for generating passwords, keys, etc.


import random
import string


# Creates a string using random characters at a specific length.
# Choose to include one, some, or all of the following:
# 1 = Letters, 2 = Numbers, 3 = Symbols, 4 = Uppercase Letters
# Ex: 24 would be uppercase letters and numbers.

# Including both 1 and 4 is not a part of being the person Mr. Rogers
# knew you could be.

### string.punctuation would be for symbols, but I don't know which are
### acceptable in a password and which aren't.  Will revisit.

def randomString(characters = 123, length = 8):
    characters = str(characters)
    # Include or don't include letters, numbers, symbols
    letters = numbers = symbols = upper = ""
    if "1" in characters:
        letters = string.ascii_letters
    if "2" in characters:
        numbers = string.digits
    if "3" in characters:
        symbols = "!#$%&()*+/<=>?[]^_`{}~"
    if "4" in characters:
        upper = string.ascii_uppercase
    # Combine desired character options
    characterOptions = letters + numbers + symbols + upper
    # Graceful error if 1, 2, and/or 3 was not entered
    if characterOptions == "":
        print("Error: randomString() expects 1234.  Input not found.")
        return
    # Return length number of random characters
    return ''.join(random.SystemRandom().choice(characterOptions) \
        for i in range(length))


def loremIpsumSentence(
        stringType = 1, minString = 2, maxString = 10, minSentence = 5,
        maxSentence = 20):
    words = []
    for i in range(minSentence, maxSentence):
        words.append(randomString(stringType, 
        random.randint(minString, maxString)))
    sentence = " ".join(words) + ".  "
    return sentence


    # x = (randomString(str(stringType), random.randint(minString, maxString)) + " ") for i in random.randint(minSentence, maxSentence) + ".  "


# Demonstrate randomString()
print("20 random letters, numbers, and symbols:")
print(randomString(123, 20))
print("")
print("")

print("Random product key (uppercase and numbers).  Five sets of " + \
    "six characters separated by dashes:")
productKey = []
for i in range(5):
    productKey.append(randomString(24, 6))
print("-".join(productKey))
print("")
print("")


print("Custom lorem ipsum (can be used for other languages):")
print(loremIpsumSentence())
