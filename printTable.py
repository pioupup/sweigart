
def printTable(tableData):
	colWidths = [0] * len(tableData)
	for col in range(len(tableData)):
		for row in range(len(tableData[col])):
			if colWidths[col] < len(tableData[col][row]):
				colWidths[col] = len(tableData[col][row])
	for row in range(len(tableData[col])):
		for col in range(len(tableData)):
			print(tableData[col][row].rjust(colWidths[col]), end=' ')
		print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)