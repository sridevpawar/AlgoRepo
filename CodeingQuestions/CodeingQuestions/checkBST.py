from myTree import myTree

def checkBST(root):
    if root == None: return True
    res = True
    if root.left != None:
        if root.left.data > root.data:
            res = False
    if root.right != None:
        if root.right.data <= root.data:
            res = False

    return res and checkBST(root.right) and checkBST(root.left)


#str = "20 10 L 20 30 R 10 5 L 5 4 L 5 5 R 10 11 R 30 35 R"
#t = myTree(None)
#root = t.makeTreeFromString(str)
#print(checkBST(root))
