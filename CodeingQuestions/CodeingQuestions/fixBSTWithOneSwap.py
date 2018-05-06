from myTree import myTree
from checkBST import checkBST
import sys
def fixBSTWithOneSwap(root):
    issueNodes = []
    findIssueNode(root, 0, sys.maxsize)

def findIssueNode(root, minAllowed, maxAllowed):
    if root == None: return True
    leftIssue = rightIssue = False

    if root.data <= minAllowed or root.data > maxAllowed:
        return root

    while leftIssue != True or rightIssue != True:
        if leftIssue != True: leftIssue = findIssueNode(root.left, minAllowed, root.data)
        if rightIssue != True: rightIssue = findIssueNode(root.right, root.data, maxAllowed)

        if rightIssue != True: 
            if rightIssue.data <= minAllowed or rightIssue.data > maxAllowed:
                return rightIssue
            else:
                swap(root, rightIssue)

        if leftIssue != True: 
            if leftIssue.data <= minAllowed or leftIssue.data > maxAllowed:
                return leftIssue
            else:
                swap(root, leftIssue) 

    return True

    
def swap(root, issueNode):
    root.data, issueNode.data = issueNode.data, root.data



treeString = "10 5 L 10 8 R 5 2 L 5 20 R"
t = myTree(None)
root = t.makeTreeFromString(treeString)
print(checkBST(root))
fixBSTWithOneSwap(root)
print(checkBST(root))