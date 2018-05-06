from myTree import myTree
from myStack import myStack
def IsTreeSymmetric(t1, t2):
    t1InOrder = t1.inOrderTraversal().split(" ")
    t2InOrder = t2.inOrderTraversal().split(" ")
    t2InverseOrder = t2.inverseInOrderTraversal().split(" ")
    indexT1InOrder = indexT2InOrder = indexT2InverseOrder = 0
    usingInverse = True if t1InOrder[1] == t2InverseOrder[1] else False
    notFound = False
    rootVal = myStack(len(t1InOrder))
    rootVal.push(t1InOrder[0])
    while indexT1InOrder < len(t1InOrder):
        if usingInverse:
            if indexT2InverseOrder < len(t2InverseOrder) and t1InOrder[indexT1InOrder] == t2InverseOrder[indexT2InverseOrder]:
                indexT2InverseOrder += 1
                notFound = False
            else:
                if notFound == True: 
                    return False
                indexT2InOrder = t2InOrder.index(t1InOrder[indexT1InOrder - 1]) + 1
                rootVal = t1InOrder[indexT1InOrder - 1]
                indexT1InOrder -= 1
                usingInverse = False
                notFound = True
        else:
            if indexT2InOrder < len(t2InOrder) and t1InOrder[indexT1InOrder] == t2InOrder[indexT2InOrder]:
                indexT2InOrder += 1
                notFound = False
            else:
                if notFound == True: 
                    return False
                indexT2InverseOrder = t2InverseOrder.index(t1InOrder[indexT1InOrder - 1]) + 1
                indexT1InOrder -= 1
                usingInverse = True
                notFound = True

        indexT1InOrder += 1

    return True





str = "10 12 L 10 13 R 12 6 L 12 8 R 6 21 L 6 16 R 21 33 R 16 24 L 8 26 L 13 5 L 13 4 R 5 28 L 5 39 R 28 94 L 28 74 R 39 73 L 39 61 R 4 31 L 4 42 R 42 51 L"
t1 = myTree(None)
root1 = t1.makeTreeFromString(str)
str = "10 13 L 10 12 R 13 5 L 13 4 R 5 39 L 5 28 R 39 61 L 39 73 R 28 94 L 28 74 R 4 42 L 4 31 R 42 51 R 12 8 L 12 6 R 8 26 R 6 21 L 6 16 R 21 33 R 16 24 L"
t2 = myTree(None)
root2 = t2.makeTreeFromString(str)
print(IsTreeSymmetric(t1, t2))