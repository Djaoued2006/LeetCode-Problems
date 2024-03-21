from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#time : 22ms
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        return nodes[len(nodes) // 2]