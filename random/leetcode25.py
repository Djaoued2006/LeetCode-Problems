#time: 39ms beats: 79.71%
#leetcode problem: 25. Reverse Nodes in k-Group

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def Listify(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(curr.val)
            curr = curr.next
        
        return nodes
    

def fromList(head: Optional[ListNode], nums: list[int]):
        head = ListNode(nums[0])
        
        curr = head 

        for num in nums[1:]:
            curr.next = ListNode(num)
            curr = curr.next
    
        return head

class Solution:
    def reverseList(self , head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = ListNode(10)
        node.next = head

        prev = node
        curr = head

        count = 1

        temp = curr

        while curr:
            if not temp:
                break 
                
            if count == k:
                next = temp.next
                temp.next = None 
                prev.next = None
                
                curr = self.reverseList(curr)
                curr.next = next
                prev.next = temp

                count = 1
                prev = curr
                curr = curr.next
                temp = curr
            else:
                temp = temp.next
                count += 1
        
        return node.next
    

head = ListNode()
nums = [i for i in range(1,6)]
head = fromList(head, nums)
head = Solution().reverseKGroup(head , 1)
print(head.Listify())
