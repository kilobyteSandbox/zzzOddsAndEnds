#! python3

# regexPasswordChecker.py
# Checks a password to see if it is worthy*.
# *worthiness determined by a fairly weak set of criteria.


import re


# Password requirements:
# 8 to 20 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit


# Regex pattern to check password requirements.
# Long version of regex pattern below for testing on a regex tester:
# (?=[^A-Z]*[A-Z])(?=[^a-z]*[a-z])(?=\D*\d).{8,20}
password_regex = re.compile(r"""(
    (?=[^A-Z]*[A-Z])    # At least one uppercase letter
    (?=[^a-z]*[a-z])    # At least one lowercase letter
    (?=\D*\d)           # At least one digit
    .{8,20}             # Password is between 8 and 20 characters
    )""", re.VERBOSE)


# Check the password and return a message based on the results.
def password_checker(password):
    # If there is a match, it passes and we give pass verification.
    if password_regex.search(password) != None:
        print("This password is strong.  Like an ox.  An ox that " +\
            "has the strength of two oxen.")
    # If there isn't a match, it fails and we give a fail message.
    else:
        print("This password is weak, and disappoints your parents.")


# Demonstrate
# ===========
print("""Password requirements:
- 8 to 20 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit

""")

# Create an endless loop that asks for and verifies passwords.  Break
# out of the loop if the user enters nothing.
while True:
    print("Enter a password to test (or nothing to exit):")
    password = input()
    if password == "":
        break
    password_checker(password)
    print("\n")