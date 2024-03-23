# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None 
        curr = node

        while curr.next:
            prev = curr
            curr.val = curr.next.val
            curr = curr.next
        
        prev.next = None
    

    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def int(self , l : Optional[ListNode]) -> int:
        result = 0
        curr = l

        while curr:
            result *= 10
            result += curr.val
            curr = curr.next
        
        return result 

    def linkedlist(self, n: int) -> Optional[ListNode]:
        node = ListNode(n % 10)
        node.next = None

        if not n:
            return node
        
        n //= 10

        while n:
            newNode = ListNode(n % 10)
            newNode.next = node
            node = newNode
            n //= 10
        
        return node
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 , num2 = self.int(l1), self.int(l2)

        result = num1 + num2

        print(result)

        return self.linkedlist(result)
        




        