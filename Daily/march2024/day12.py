#time : 204ms
#leetcode problem: 1171. Remove Zero Sum Consecutive Nodes from Linked List

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def toList(nums: list[int]):
    head = None 
    l = len(nums)
    i = 0

    if l:
        head = ListNode(nums[0])
    else:
        return None
    
    curr = head
    for i in range(1 , l):
        curr.next = ListNode(nums[i])
        curr = curr.next
    
    return head


class Solution:    
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        values = []
        
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        left , right = 0 , 0

        l = len(values) #for length
        s = 0 #for sum

        while left < l:                    
            s += values[right]

            if not s:
                if not left:
                    values[:] = values[right+1:]
                else:
                    values[:] = values[:left] + values[right+1:]
                
                l = len(values)
                
                s = 0
                left = 0
                right = left 
            else:
                right += 1
            
            if right == l:
                left += 1
                right = left
                s = 0
        
        head = toList(values)
        return head