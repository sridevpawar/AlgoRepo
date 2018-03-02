from myObject import myClass
class myLinkedList:
    _head = None
    _list = []

    def __init__(self, type, size, list=[]):
        if len(list) <= 0:
            if type == "int":
                self._list = [x for x in range(1,size)]
            elif type == "str":
                self._list= ["Hi" for x in range(1,size)]
        else:
            self._list = list
    
    def makeLinkedList(self):
        last = None
        head = None
        for i in self._list:
            new = myClass(i)
            if head == None:
                head = new
                last = new
            else:
                last._next = new

            last = new
            
        self._head = head
        return self._head

    def delet(node, head):
        current = head
        while(current != None):
            if current._next == node:
                current._next = current._next._next
                return True
            current = current._next

    def printLL(head):
        current = head
        while(current != None):
            print("number: {0}, string: {1}, next: {2}".format(current._number, current._string, current._next))
            current = current._next

    def newLL(type, size, list=[]):
        val = myLinkedList(type, size, list)
        val.makeLinkedList()
        return val