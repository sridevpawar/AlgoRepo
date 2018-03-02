from myObject import myClass
from myStack import myStack

class plateStacks:
    stacks = []
    top = -1
    eachCapacity = 0
    numPlates = 0
    
    def __init__(self, stackSize, numStacks):
        self.eachCapacity = stackSize
        self.numPlates = numStacks
        self.stacks = [myStack(stackSize) for x in range(numStacks)]

    def isFull(self):
        return self.stacks[-1:][0].isFull()

    def isEmpty(self):
        return self.top < 0

    def printStack(self):
        if self.isEmpty():
            return False

        for i in range(self.numPlates):
            self.stacks[i].printStack()

    def puchAt(self, index,val):
        if self.isFull() or self.stacks[index].isFull():
            return

        self.stacks[index].push(val)
            

    def push(self, val):
        if self.isFull():
            return
        
        self.top = self.top if self.top >= 0 else 0
        if self.stacks[self.top].isFull():
            self.top += 1
            self.stacks[self.top].push(val)
        else:
            self.stacks[self.top].push(val)
            
    def pop(self):
        if self.isEmpty():
            return False

        val =  self.stacks[self.top].pop()
        if self.stacks[self.top].isEmpty():
            self.top -= 1
        
        return val

    def peak(self):
        if self.isEmpty():
            return False

        return self.stacks[top].peak()