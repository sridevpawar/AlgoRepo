def processImage(matrix, x, y, k):
    chnageAdjacentPixel(matrix, x, y, k)
def chnageAdjacentPixel(matrix, x, y, k):
    currentValue = matrix[x][y]
    matrix[x][y] = k
    if y + 1 < len(matrix[x]) and matrix[x][y + 1] == currentValue:
        chnageAdjacentPixel(matrix, x, y + 1, k)
    if y - 1 >= 0 and matrix[x][y - 1] == currentValue:
        chnageAdjacentPixel(matrix, x, y - 1, k)
    if x + 1 < len(matrix) and matrix[x + 1][y] == currentValue:
        chnageAdjacentPixel(matrix, x + 1, y, k)
    if x - 1 >= 0 and matrix[x - 1][y] == currentValue:
        chnageAdjacentPixel(matrix, x - 1, y, k)


def printMatrix(matrix):
    for row in matrix:
        print((" {} "*len(row)).format(*[col for col in row]))

matrix = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 2, 0],
          [1, 0, 0, 1, 1, 2, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]];
printMatrix(matrix)
print("-"*50)
processImage(matrix, 4, 4, 3)
printMatrix(matrix)