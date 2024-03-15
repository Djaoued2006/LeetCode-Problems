from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self , head : Optional[ListNode]) -> int :
        
        result = 0
        node = head
        
        while node:
            result += 1
            node = node.next


        return result
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead
        """

        listLength = Solution().length(head)
        nodes = [None] * listLength
        node = head
        i = 0

        while node:
            nodes[i] = node
            node = node.next
            i += 1

        left , right = 0 , listLength - 1

        while left < right:
            temp = nodes[left].next
            nodes[left].next = nodes[right]
            nodes[right].next = temp
            left += 1
            right -= 1

        nodes[listLength // 2].next = None


