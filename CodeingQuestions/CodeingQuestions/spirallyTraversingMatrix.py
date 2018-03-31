import math

def printMatrix(matrix):
    for row in matrix:
        print((" {} "*len(row)).format(*[col for col in row]))

def printSpirallyTraversingMatrix(matrix):
    layer = math.ceil(len(matrix[0])/2)
    size = len(matrix[0])

    for l in range(layer):
        if size <= 1:
            print(matrix[l][l])

        for s in range(size - 1):
            print(matrix[l][l+s])

        for s in range(size - 1):
            print(matrix[l+s][size -1 + l])

        for s in reversed(range(1, size)):
            print(matrix[size - 1 + l][l+s])

        for s in reversed(range(1, size)):
            print(matrix[l+s][l])

        size -= 2


val1 = [[2,5,4,6],[8,7,3,3],[3,4,5,0],[3,0,5,7]]
val2 = [[2,5,0],[8,7,3],[3,4,5]]
val3 = [[2,5,4,8,3],[8,7,3,1,6],[0,4,5,2,1],[3,1,5,2,4],[3,4,1,2,4]]
val4 = [[0,5,4,8,3],[8,7,3,1,4],[3,4,2,4,3],[3,1,5,2,4],[3,4,1,2,4]]
val5 = [[8,3,3,3,3,0],[2,4,8,3,3,3],[3,0,2,4,8,3],[3,3,3,0,2,4],[8,3,3,3,3,0],[2,4,6,8,6,3]]
#printMatrix(val1)
#printSpirallyTraversingMatrix(val1)
#print("-"*20)
#printMatrix(val2)
#print("-"*10)
#printSpirallyTraversingMatrix(val2)
#print("-"*20)
#printMatrix(val3)
#print("-"*10)
#printSpirallyTraversingMatrix(val3)
#print("-"*20)
#printMatrix(val4)
#print("-"*10)
#printSpirallyTraversingMatrix(val4)
#print("-"*20)
printMatrix(val5)
#print("-"*10)
printSpirallyTraversingMatrix(val5)
#print("-"*20)