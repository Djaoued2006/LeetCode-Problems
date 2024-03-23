#leetcode problem : 92. Reverse Linked List II
#time : 29ms beats : 91.45%

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None , head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev    
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        node = ListNode(500)
        node.next = head

        prev = node
        currLeft = head

        #getting the left node!
        count = 1
        while count < left:
            count += 1
            prev = currLeft
            currLeft = currLeft.next
        
        #getting the right node!
        currRight = currLeft
        while count < right:
            count += 1
            currRight = currRight.next
        
        #extracting the list wanted!

        temp = currRight.next
        prev.next = None
        currRight.next = None

        #reversing the list:
        last = currLeft
        currLeft = self.reverseList(currLeft)

        prev.next = currLeft
        last.next = temp
    
        return node.next

