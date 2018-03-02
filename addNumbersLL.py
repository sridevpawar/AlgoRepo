import  myLinkedList
from myObject import myClass
LL = myLinkedList.myLinkedList

def addLL(head1, head2):
    current1 = head1
    current2 = head2
    answerHead = None
    ansRunner = None
    carry = 0

    while(current1 != None or current2 != None or carry == 1):
        if current1 != None:
            a = current1._number
            current1 = current1._next
        else:
            a = 0

        if current2 != None:
            b = current2._number
            current2 = current2._next
        else:
            b = 0

        r = a + b + carry

        carry = 0
        if r >= 10:
            r = r - 10
            carry = 1

        val = myClass(r)
        if answerHead == None:
            answerHead = val
            ansRunner = val
        else:
            ansRunner._next = val
            ansRunner = val

    return answerHead
        

def main():
    myLL1 = LL.newLL(None, None, [3,9])
    myLL2 = LL.newLL(None, None, [1,9,4])
    LL.printLL(myLL1._head)
    print("+"*60)
    LL.printLL(myLL2._head)
    print("="*60)
    LL.printLL(addLL(myLL1._head, myLL2._head))
    print("/"*60)

main()

