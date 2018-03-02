import  myLinkedList
LL = myLinkedList.myLinkedList

def findDupe(head):
    current = head
    result = []
    while(current != None):
        if findFrequesncy(current) > 0:
            result.append(current._number)

        current = current._next

    return result

def findFrequesncy(node):
    current = node._next
    value = node._number
    counter = 0
    while(current != None):
        if current._number == value:
            counter =+ 1
            LL.delet(current, node)
        current = current._next

    return counter

def main():
    myLL = LL.newLL(None, None, [10, 20, 40, 30, 30, 60, 80, 80, 90, 10, 70])
    LL.printLL(myLL._head)
    print(findDupe(myLL._head))
    LL.printLL(myLL._head)

main()
