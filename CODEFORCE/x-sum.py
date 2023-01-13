from collections import defaultdict

#size of input
inputSize = int(input())

#array to store the answer
answer = []

for _ in range(inputSize):
    #the diagonal input size
    diagonals = defaultdict(int)
    antiDiagonals = defaultdict(int)

    #input the row and column size
    rowSize, columnSize = list(map(int,input().split()))

    #the grid
    grid = [[0]*columnSize for i in range(rowSize)]

    #input the grid
    for rowIndex in range(rowSize):
        #input the row
        row = list(map(int, input().split()))

        for columnIndex in range(columnSize):
            #record the grid
            grid[rowIndex][columnIndex] = row[columnIndex]

            #record the diagonal data
            diagonals[rowIndex-columnIndex] += row[columnIndex]
            antiDiagonals[rowIndex + columnIndex] += row[columnIndex]

    maximumPlacement = 0
    for rowIndex in range(rowSize):
        for columnIndex in range(columnSize):
            #the sum of the diagonals
            placementSum = diagonals[rowIndex-columnIndex] + antiDiagonals[rowIndex + columnIndex] - grid[rowIndex][columnIndex]
            maximumPlacement = max(maximumPlacement, placementSum )

    #add to the answer
    answer.append(maximumPlacement)


for value in answer:
    print(value)
