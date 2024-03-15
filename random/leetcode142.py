# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = 0
        node = head
        nodes = dict()

        while node:
            if (node in nodes):
                return node
            else:
                nodes[node] = pos
            
            node = node.next
            pos += 1
        
        return None

