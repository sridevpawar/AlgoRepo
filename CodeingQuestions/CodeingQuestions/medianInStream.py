import copy
class medianInStream:
    def __init__(self):
        self.stream = []
        self.mE = []

    def insert(self, n):
        self.stream.append(n)
        if len(self.stream) <= 2: 
            self.mE = copy.copy(self.stream)
            self.printMedian()
            return

        newValGreaterThanME = self.greaterThanME(n)
        if newValGreaterThanME == 1:
            if len(self.mE) == 2:
                self.mE = [max(self.mE[0], self.mE[1])]
            else:
                self.mE = [self.mE[0], self.findNext(self.mE[0], 'G')]
        elif newValGreaterThanME == -1:
            if len(self.mE) == 2:
                self.mE = [min(self.mE[0], self.mE[1])]
            else:
                self.mE = [self.mE[0], self.findNext(self.mE[0], 'L')]
        elif newValGreaterThanME == 0:
            self.mE = [n]

        self.printMedian()

    def findNext(self, n, LorG):
        nextG = 0
        nextL = 0
        countG = 0
        countL = 0
        countS = 0
        for x in self.stream:
            if x > n: 
                countG += 1
                nextG = min(nextG, x)
            elif x < n: 
                countL += 1
                nextL = max(nextL, x)
            elif x == n: countS += 1

        if LorG == 'G':
            if countL + countS <= countG:
                return nextG
            else:
                return n
        elif LorG == 'L':
            if countG + countS <= countL:
                return nextL
            else:
                return n

    def greaterThanME(self, n):
        if len(self.mE) == 1:
           return 1 if n >= self.mE[0] else -1
        if len(self.mE) == 2: 
            return 1 if n > self.mE[0] and n > self.mE[1] else -1 if n < self.mE[0] and n < self.mE[1] else 0

    def printMedian(self):
        if len(self.mE) == 1: print(self.mE[0])
        if len(self.mE) == 2: print((self.mE[0] + self.mE[1])/2)


arr = [5, 15, 1, 3]
obj = medianInStream()
for x in arr:
    obj.insert(x)