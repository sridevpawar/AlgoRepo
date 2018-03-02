from myObject import treeNode
import math

def BST(numbers):
    if len(numbers) <= 0:
        return None
    rootIndex = math.floor(len(numbers) / 2)
    root = treeNode(numbers[rootIndex])
    root.left = BST(numbers[:rootIndex])
    root.right = BST(numbers[rootIndex + 1:])
    return root
    