#leetcode problem : 203. Remove Linked List Elements

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node = ListNode(-1)
        node.next = head

        curr = head
        prev = node

        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr 
                curr = curr.next
            
        return node.next