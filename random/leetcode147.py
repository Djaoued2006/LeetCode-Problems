from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        done = False

        while curr:
            value = curr.val
            temp = head 

            while (temp != curr):
                if (value >= temp.val):
                    temp = temp.next
                else:
                    break
            
            done = (curr != temp)
            
            curr.val = temp.val
            temp.val = value

            if (not done):
                curr = curr.next
    
        return head
        

            

            
