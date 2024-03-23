#leetcode problem : 138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        newList = Node(head.val)
        newList.next = None
        newCurr = newList
        curr = head.next

        while curr:
            newCurr.next = Node(curr.val)
            newCurr = newCurr.next
            curr = curr.next

        curr = head
        newCurr = newList

        while curr:
            if curr.random is None:
                newCurr.random = None
            else:
                temp = head
                tempCurr = newList
                
                while temp != curr.random:
                    temp = temp.next
                    tempCurr = tempCurr.next
                
                newCurr.random = tempCurr

            curr = curr.next
            newCurr = newCurr.next

        return newList
