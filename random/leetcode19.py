from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def length(self , head : Optional[ListNode]) -> int:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        return count
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if (not head):
            return head
        
        if (not head.next):
            return head.next 
        
        
        listlen = Solution().length(head)

        if (n >= listlen):
            return head.next 
        
        i = 1 
        curr = head

        while (i < listlen - n):
            i += 1
            curr = curr.next 
        
        temp = curr.next 
        curr.next = temp.next 

        return head 


