class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None
        inter = head
        temp = head
        prev = None
        count = 0
        while(temp is not None):
            count += 1
            if count <= n:
                temp = temp.next
            else:
                prev = inter
                inter = inter.next
                temp = temp.next
        if count == n:
            return head.next
        prev.next = inter.next
        del(inter)
        return head