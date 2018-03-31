class stream:

    def __init__(self, k):
        self.stream = []
        self.k = k
        self.kd = {}
        for i in range(1, k + 1):
            self.kd[i] = -1

    def insert(self, x):
        self.stream.append(x)
        if x > self.kd[self.k]:
            self.addK(x)
        print(self.kd[self.k])

    def addK(self, x):
        for i in reversed(range(1, self.k + 1)):
            if x == self.kd[i]:
                return
            if x < self.kd[i]:
                for j in reversed(range(i + 1, self.k)):
                    self.kd[j + 1] = self.kd[j]
                self.kd[i + 1] = x
                break

        if self.kd[1] < x:
            for j in reversed(range(1, self.k)):
                    self.kd[j + 1] = self.kd[j]
            self.kd[1] = x


        



s1 = [10, 20, 11, 70, 50, 40, 100, 5]
k1 = 3
so = stream(k1)
for s in s1:
    so.insert(s)