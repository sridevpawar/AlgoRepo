class myTree:

    def __init__(self, root):
        self.root = root

    def height(self,root):
        if root == None:
            return 0

        return max(height(root.left),height(root.right)) + 1

    def printTree(self):

        
            