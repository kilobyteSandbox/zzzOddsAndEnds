#! python 3

# separatedlist.py
# ================
# Takes a string and adds a new line whenever the designated character is found.
# Does something else already do this?  Probably.  Better?  Almost certainly.


# Example usage:
# "Apple,banana,carrot"

# becomes:

# "Apple
# banana
# carrot"


import pyperclip


# Takes a list from the clipboard, then creates a new line whenever a seperator appears.
def separated_list(seperator):
	copied_list = pyperclip.paste()
	new_list = ""
	for i in copied_list:
		# If we run into the seperator character, create a new line.
		if i == seperator:
			new_list += "\n"
		# If we run into a new line, delete that new line.
		elif i == "\n":
			new_list += ""
		# Otherwise, copy the old list to the new list.
		else:
			new_list += i
	return new_list


# Print the modified list with new lines.
print(separated_list(";"))