import  myLinkedList
LL = myLinkedList.myLinkedList

def findDupeWithIndex(head):
    current = head
    index = [False for x in range(101)]
    result = []
    while(current != None):
        if index[current._number] == True:
            result.append(current._number)

        index[current._number] = True
        current = current._next

    return result

def main():
    myLL = LL.newLL(None, None, [10, 20, 40, 30, 30, 60, 80, 80, 90, 10, 70])
    LL.printLL(myLL._head)
    print(findDupeWithIndex(myLL._head))
    LL.printLL(myLL._head)

main()

