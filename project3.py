from linkedlist import Unorderedlist
import random
def insertionlinksort(alist):
    previous = alist.head
    current = alist.head.next
    while current != None:
        current =previous.next
        while current != None and current.data >= previous.data:
            current = current.next
            previous = previous.next
        if current == None:
            break
        previous.next = current.next
        temp = alist.head
        if temp.data > current.data:
            current.next = alist.head
            alist.head = current
        else:
            while temp.next.data < current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
u=Unorderedlist()
for i in range(10):
    u.add(random.randrange(1,20))
u.printlist()

insertionlinksort(u)
u.printlist()
