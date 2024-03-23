from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(1000)
        node.next = head

        prev = node
        curr = head

        while curr:
            next = curr.next
            if not next:
                break

            prev.next = next
            curr.next = next.next
            next.next = curr
            prev = curr
            curr = curr.next
        
        return node.next

        

            
        