from myObject import treeNode
from myStack import myStack
class myTree:

    def __init__(self, root):
        self.root = root
        def inOrderSelector(root, stack):
            if root.right != None: stack.push(root.right)
            if root.left != None: stack.push(root.left)
            return root.data
        def inverseInOrderSelector(root, stack):
            if root.left != None: stack.push(root.left)
            if root.right != None: stack.push(root.right)
            return root.data
        self.inOrderSelector = inOrderSelector
        self.inverseInOrderSelector = inverseInOrderSelector

    def height(self,root):
        if root == None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def nodeExists(self, root, data):
        if root == None: return None
        if root.data == data: return True
        return self.nodeExists(data, root.left) or self.nodeExists(data, root.right)

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
                if current.left != None and current.left.data == parent:
                    current = current.left
                elif  current.right != None and current.right.data == parent:
                    current = current.right
                else:
                    current = current.parent

        return self.root

    def inOrderTraversal(self):
        return self.orderTraversal(self.root, key=self.inOrderSelector)

    def inverseInOrderTraversal(self):
        return self.orderTraversal(self.root, key=self.inverseInOrderSelector)

    def orderTraversal(self, root, key=None):
        height = self.height(root)
        stack = myStack(height)
        result = str(key(root, stack))
        while not stack.isEmpty():
            currentRoot = stack.pop()
            result += " " + str(key(currentRoot, stack))

        return result


        
            