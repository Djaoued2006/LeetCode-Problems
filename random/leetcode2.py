from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def toInteger(self , l : Optional[ListNode]) -> int:
        result,  i = 0 , 0
        curr = l

        while curr:
            result += curr.val * (10**i)
            i += 1
            curr = curr.next
        
        return result

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 , num2 = self.toInteger(l1) , self.toInteger(l2)
        result = num1 + num2

        head = ListNode(result % 10)

        result //= 10

        head.next = None 
        last = head

        while result:
            last.next = ListNode(result % 10)
            last = last.next
            result //= 10
        
        return head


