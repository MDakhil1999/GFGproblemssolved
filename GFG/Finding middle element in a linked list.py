def findMid(head):
    temp1 = head
    temp2 = head
    while(temp1.next is not None and temp2.next is not None):
        if temp2.next.next is not None:
            temp1 = temp1.next
            temp2 = temp2.next.next
        else:
            return temp1.next.data
    return temp1.data