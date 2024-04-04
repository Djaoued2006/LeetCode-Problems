from typing import Optional

#time: 36ms beats: 65.45%
#leetcode problem: 86. Partition List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #those nodes are fake
        smaller, biggerOrEqual = ListNode(10) , ListNode(20)
        LastSmall, LastBig = smaller, biggerOrEqual

        curr = head

        while curr:
            next = curr.next
            curr.next = None

            if curr.val < x:
                LastSmall.next = curr
                LastSmall = LastSmall.next
            else:
                LastBig.next = curr
                LastBig = LastBig.next
            
            curr = next
        
        if not smaller.next:
            return biggerOrEqual.next
        
        smaller = smaller.next
        LastSmall.next = biggerOrEqual.next

        return smaller

            

        