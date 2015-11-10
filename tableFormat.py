#! python3

# tableFormat.py
# Takes a list of lists and formats it into an aligned table.


# Finds the longest item in a list and returns the length.
def longest_list(stringList):
    return len(max(stringList, key = len))


# Formats a list of lists into a table.
def print_table(tableList, padding = 3):
    # Find the longest string in each sublist (column width per column).
    columnWidths = []
    for i in tableList:
        columnWidths.append(longest_list(i))
    # Find the longest sublist (column length in rows).
    # Not currently configured to take multiple column lengths, but I
    # may revisit this so the flexibility is included for now.
    columnHeight = longest_list(tableList)
    # For each row in the column (top to bottom)
    for row in range(columnHeight):
        # For each column (left to right)
        for column in range(len(tableList)):
            # Print the cell in column/row, left adjust according to the
            # max width in that column, and add padding.
            print((tableList[column][row]).ljust(columnWidths[column] +\
                padding), end = "")
        print("\n")


# Demonstrate print_table
tableData = [['COLORS', 'Blue', 'Red', 'Orange'],
             ['SHAPES', 'Circle', 'Square', 'Line'],
             ['TRANSPARENCY', 'Opaque', 'Transparent', 'Partial']]


print_table(tableData)