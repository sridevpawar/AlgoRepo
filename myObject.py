class myClass:
    _string = ""
    _number = 0
    _next = None
    _prev = None
    _links = []

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            foundOneArg = True
            argValue = args[0]
        elif len(args) == 0:
            return


        if foundOneArg and isinstance(argValue, int):
            self._number = argValue

        if foundOneArg and isinstance(argValue, str):
            self._string = argValue

        if foundOneArg and isinstance(argValue, list):
            self._links = argValue

class node:
    
    def __init__(self, data):
        self.data = data
        self.list = []

class treeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
