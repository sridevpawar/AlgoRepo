from myTree import myTree
def binaryTreeToDLL(root):
    if root == None: return None, None
    if isLeaf(root): return root, root

    firstL, lastL = binaryTreeToDLL(root.left)
    firstR, lastR = binaryTreeToDLL(root.right)

    root.left = firstR
    root.right = lastL
    if lastL != None: lastL.left = root
    if firstR != None: firstR.right = root

    if firstL == None: firstL = root
    if lastR == None: lastR = root
    return firstL, lastR




def isLeaf(node):
    if node.left == None and node.right == None: return True
    return False


str = "10 12 L 10 15 R 12 25 L 12 30 R 15 36 L"
t = myTree(None)
root = t.makeTreeFromString(str)
dll,x = binaryTreeToDLL(root)
while dll != None:
    print(dll.data, "<->")
    dll = dll.left