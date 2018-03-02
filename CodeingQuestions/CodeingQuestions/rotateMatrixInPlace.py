import math

def printMatrix(matrix):
    for row in matrix:
        print((" {} "*len(row)).format(*[col for col in row]))


def rotateMatrix(matrix):
    if len(matrix) <= 0 or len(matrix[0]) <= 0:
        return

    for layer in range(math.ceil(len(matrix)/2)):
        for col in range(len(matrix) - 1 - (2*layer)):
            temp = matrix[layer][col + layer]
            matrix[layer][col + layer] = matrix[col + layer][(len(matrix) - 1) - layer]
            matrix[col + layer][(len(matrix) - 1) - layer] = matrix[(len(matrix) - 1) - layer][(len(matrix) - 1) - col + layer]
            matrix[(len(matrix) - 1) - layer][(len(matrix) - 1) - col + layer] = matrix[(len(matrix) - 1) - col + layer][layer]
            matrix[(len(matrix) - 1) - col][layer] = temp

    return matrix





val1 = [[2,5,4],[8,7,3],[3,4,5],[3,0,5],[3,4,0]]
val2 = [[2,5,0,8,3],[8,7,3,1,6],[3,4,5,2,1]]
val3 = [[2,5,4,8,3],[8,7,3,1,6],[0,4,5,2,1],[3,1,5,2,4],[3,4,1,2,4]]
val4 = [[0,5,4,8,3],[8,7,3,1,4],[3,4,2,4,3],[3,1,5,2,4],[3,4,1,2,4]]
val5 = [[8,3],[3,3],[3,0],[2,4],[8,3],[3,3],[3,0],[2,4],[8,3],[3,3],[3,0],[2,4],[8,3],[3,3],[3,0],[2,4]]
printMatrix(val1)
print("-"*20)
printMatrix(rotateMatrix(val1))
print("-"*50)
printMatrix(val2)
print("-"*20)
printMatrix(rotateMatrix(val2))
print("-"*50)
printMatrix(val3)
print("-"*20)
printMatrix(rotateMatrix(val3))
print("-"*50)
printMatrix(val4)
print("-"*20)
printMatrix(rotateMatrix(val4))
print("-"*50)
printMatrix(val5)
print("-"*20)
printMatrix(rotateMatrix(val5))
print("-"*50)
