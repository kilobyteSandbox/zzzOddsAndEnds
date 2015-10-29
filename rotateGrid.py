# Goal: Print out the image in "grid" rotated 90 degrees to the right.


# These lists make up the image that will be rotated.
alien = [
		['.','.','.','O','O','O','.'], 
		['.','.','O','O','.','.','.'], 
		['.','O','O','O','O','.','O'], 
		['O','O','O','O','O','O','O'], 
		['.','O','O','O','O','.','.'], 
		['.','X','X','X','X','.','.'], 
		['X','X','X','X','X','X','X'], 
		['.','X','X','X','X','.','X'], 
		['.','.','X','X','.','.','.'], 
		['.','.','.','X','X','X','.'], 
		]


# Rotate grid 90 degrees right and print
def printRotatedGrid(grid):
	# Figure out how many x values we have
	maxX = len(grid[0])
	# Figure out how many y values we have
	maxY = len(grid)
	# Min to max X value
	for xValue in range(maxX):
		# Min to max Y value 
		for yValue in range(maxY):
			# Grid goes left to right, min X to max X
			# Grid goes TOP to BOTTOM, min y to max y
			# Adjust maxY by 1 (len() starts at 1, range() starts at 0)
			# To rotate right, print row of maxY to minY,
			# then increase x by 1 and repeat
			print(grid[maxY - 1 - yValue][xValue], end="")
		print("")


# Demonstrate function
printRotatedGrid(alien)
