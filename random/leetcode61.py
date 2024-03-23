from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        
        node = ListNode(10101)
        node.next = head
        
        #getting length and the last node:
        l = 1
        curr = head
        while curr.next:
            l += 1
            curr = curr.next
        
        k = k % l

        if not k:
            return head
        
        last = curr
        
        i = 1
        curr = head
        while (i < l - k):
            curr = curr.next
            i += 1
        
        temp = curr.next
        curr.next = None
        last.next = head
        head = temp
    
        return head 