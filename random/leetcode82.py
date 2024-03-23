#leetcode problem : 82. Remove Duplicates from Sorted List II
#time : 33ms beats : 91.14%

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(-101)
        node.next = head

        prev = node
        curr = head

        if curr:
            while curr.next:
                if curr.next.val == curr.val:
                    curr = curr.next
                else:
                    if prev.next != curr:
                        curr = curr.next
                        prev.next = curr
                    else:
                        prev = curr
                        curr = curr.next
            
            if prev.next != curr:
                curr = curr.next
                prev.next = curr
            
        return node.next
                
                
