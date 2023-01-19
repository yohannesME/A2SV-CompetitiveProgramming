from collections import defaultdict

#input the row size and column size
rowSize, columnSize = list(map(int,input().split()))

crosswordGrid = []

for _ in range(rowSize):
    crosswordGrid.append(list(input()))

#answer array
filteredGrid = []

#copy the original array
for row in range(rowSize):
    filteredRow = []
    for column in range(columnSize):
        filteredRow.append(crosswordGrid[row][column])
    filteredGrid.append(filteredRow)


#change all the occurances greater than one to X in the row
for row in range(rowSize):
    rowapperance = defaultdict(list)
    for column in range(columnSize):
        rowapperance[crosswordGrid[row][column]].append(column)

    #change to x
    for letter, indices in rowapperance.items():
        if len(indices) > 1:
            for index in indices:
                filteredGrid[row][index] = 'X'

#change all the occurances greater than one to X in the column
for column in range(columnSize):
    columnapperace = defaultdict(list)
    for row in range(rowSize):
        columnapperace[crosswordGrid[row][column]].append(row)

    #change to x
    for letter, indices in columnapperace.items():
        if len(indices) > 1:
            for index in indices:
                filteredGrid[index][column] = 'X'

#display all except for X
for row in range(rowSize):
    for column in range(columnSize):
        if filteredGrid[row][column] != 'X':
            print(filteredGrid[row][column], end='')
