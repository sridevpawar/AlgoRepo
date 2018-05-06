from myObject import treeNode
class myTree:

    def __init__(self, root):
        self.root = root

    def height(self,root):
        if root == None:
            return 0

        return max(height(root.left),height(root.right)) + 1

    def makeTreeFromString(self, str):
        strArr = str.split(" ")
        self.root = treeNode(int(strArr[0]), None)
        index = 0
        current = self.root
        while index < len(strArr) and current != None:
            parent = int(strArr[index])
            child = int(strArr[index + 1])
            side = strArr[index + 2]
            if current.data == parent:
                if side == "R":
                    current.right = treeNode(child, current)
                elif side == "L":
                    current.left = treeNode(child, current)

                index += 3
            else:
                if current.left.data == parent:
                    current = current.left
                elif current.right.data == parent:
                    current = current.right
                else:
                    current = current.parent

        return self.root


        
            