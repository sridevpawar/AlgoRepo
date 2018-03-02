from myObject import myClass
from random import randint

class makeAMGraph:

    def __init__(self, size, fillIt, biDirectional):
        self.size = size
        self.nodes = [0 for _ in range(self.size)]
        for row in range(self.size):
            self.nodes[row] = [0 for _ in range(self.size)]
            
        if fillIt:
            for row in range(self.size):
                for col in range(self.size):
                    if not biDirectional and col > row:
                        break
                    if row == col:
                        self.nodes[row][col] = 1
                    else:
                        self.nodes[row][col] = randint(0,1)


       
    def printG(self):
        line = "  "
        for r in range(self.size):
            line += "{} ".format(chr(97 + r))

        print(line)
        line = ""
        for row in range(self.size):
            line += "{} ".format(chr(97 + row))
            for col in range(self.size):
                line += "{} ".format(self.nodes[row][col])

            print(line)
            line = ""
                

class makeALGraph:
    
    def __init__(self, numNodes, biDirectional):
        self.numNodes = numNodes
        self.nodes = [node(chr(randint(0,26) + 97)) for _ in range(self.numNodes)]
        for i in range(self.numNodes):
            for _ in range(randint(0,numNodes*0.2)):
                tempNode = self.nodes[randint(0, self.numNodes - 1)]
                self.nodes[i].list.append(tempNode)
                if biDirectional:
                    tempNode.list.append(self.nodes[i])


    def printG(self):
        for i in range(self.numNodes):
            line = "{} ->".format(self.nodes[i].data)
            for x in self.nodes[i].list:
                line += "{}, ".format(x.data)

            print(line)


g = makeALGraph(10, True)