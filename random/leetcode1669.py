# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getTail(self, list : ListNode) -> ListNode:
        if not list:
            return list 
        if not list.next:
            return list 
        
        curr = list 
        while curr.next:
            curr = curr.next 
        
        return curr 

        
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        tail = Solution().getTail(list2)

        if a == 0:
            for i in range(b):
                curr = curr.next
            
            tail.next = curr.next
            list1 = list2
        else:
            for i in range(a-1):
                curr = curr.next 
            
            curr2 = curr.next

            for i in range(b-a+1):
                curr2 = curr2.next 
            
            curr.next = list2
            tail.next = curr2 
        
        return list1

            
        
            
