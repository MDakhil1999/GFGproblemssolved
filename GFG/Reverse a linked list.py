class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        prev = None
        while(head):
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev