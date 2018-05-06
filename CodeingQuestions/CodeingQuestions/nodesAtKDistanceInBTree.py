from myTree import myTree
class nodesAtKDistanceInBTree:
    def __init__(self, treeString):
        t = myTree(None)
        self.treeRoot = t.makeTreeFromString(treeString)
        self.result = []

    def findNodesAtKDistance(self, target, k):
        self.k = k
        self.findNode(self.treeRoot, target)
        return self.result

    def getDownNodesAtDistance(self, root, k):
        if root == None: return None
        if k == 1: self.result.append(root.data)

        self.getDownNodesAtDistance(root.left, k - 1)
        self.getDownNodesAtDistance(root.right, k - 1)

    def findNode(self, root, target):
        if root == None: return None
        if root.data != target:
            l = self.findNode(root.left, target)
            if l == None: r = self.findNode(root.right, target)

        if root.data ==  target:
            self.getDownNodesAtDistance(root.left, self.k)
            self.getDownNodesAtDistance(root.right, self.k)
            return 0

        if l != None:
            self.getDownNodesAtDistance(root.right, self.k - 1 - l)
            return l + 1

        if r != None:
            self.getDownNodesAtDistance(root.left, self.k - 1 - r)
            return r + 1

str = "20 8 L 20 22 R 8 4 L 8 12 R 4 3 L 4 2 R 3 9 L 3 7 R 2 11 L 2 15 R 12 10 L 12 14 R 10 23 L 10 26 R 14 28 L 14 31 R 22 16 L"
obj = nodesAtKDistanceInBTree(str)
print(obj.findNodesAtKDistance(8, 3))