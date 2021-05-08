def delNode(head, k):
    # Code here
    prev = None
    count = 0
    temp = head
    if k == 1:
        return head.next
    while(temp):
        count += 1
        if count == k:
            prev.next = temp.next
            del(temp)
            return head
        prev = temp
        temp = temp.next