from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#time : 373ms
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #getting the length:
        l = 0
        curr = head

        while curr:
            curr = curr.next
            l += 1
        
        #creating the array:
        nodes = [0] * l 

        #filling the array:
        curr = head
        i = 0
        while curr:
            nodes[i] = curr.val 
            curr = curr.next
            i += 1

        maxSum = 0
        for i in range(l // 2):
            maxSum = max(maxSum , nodes[i] + nodes[l - i - 1])
        
        return maxSum

#time : 411ms
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         #using hash map
        
#         nodes = dict()
#         i = 0
        
#         curr = head
#         while curr:
#             nodes[i] = curr.val 
#             i += 1
#             curr = curr.next 
        
#         l = i 
#         maxSum = 0
#         for i in range(l // 2):
#             maxSum = max(maxSum , nodes[i] + nodes[l - i - 1])
        
#         return maxSum

#time : 584ms
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         #using another linked list:
#         new = None 
        
#         curr = head 
#         l = 0

#         while curr:
#             node = ListNode(curr.val)
#             node.next = new
#             new = node 
#             curr = curr.next 
#             l += 1
        
#         maxSum = 0
#         left, right = head , new
#         for i in range(l//2):
#             maxSum = max(maxSum , left.val + right.val)
#             left = left.next 
#             right = right.next 
        
#         return maxSum

