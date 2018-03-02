class myStack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.stackArr = []

    def isFull(self):
        if self.top >= self.capacity - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    def printStack(self):
        if self.isEmpty():
            return False

        size = self.capacity - 1
        while(size >= 0):
            isTop = "<- Top" if size == self.top else ""
            if size <= self.top:
                valprint = "{}{}".format(self.stackArr[size], " ") if self.stackArr[size] < 10 else self.stackArr[size]
            else:
                valprint = " "

            print("| {0} | {1}".format(valprint, isTop))
            size -= 1

    def push(self, val):
        if self.isFull():
            return

        self.top += 1
        self.stackArr.insert(self.top, val)

    def pop(self):
        if self.isEmpty():
            return False

        val =  self.stackArr[self.top]
        self.stackArr[self.top] = 0
        self.top -= 1
        return val

    def peak(self):
        if self.isEmpty():
            return False

        return self.stackArr[self.top]
