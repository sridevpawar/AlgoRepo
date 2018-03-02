import  myLinkedList
from myObject import myClass
LL = myLinkedList.myLinkedList

def kthElement(head, k):
    current = head
    kthRunner = head

    for x in range(k - 1):
        current = current._next

    while(current._next != None):
        current = current._next
        kthRunner = kthRunner._next

    return kthRunner._number

def main():
    myLL = LL.newLL(None, None, [x for x in range(7)])
    LL.printLL(myLL._head)
    print(kthElement(myLL._head, 3))

main()

