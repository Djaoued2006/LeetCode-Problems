from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None

        if head:
            if head.next:
                new = head.next
                head.next = new.next
            else:
                return head 
        else:
            return head
    
        tail = new
        curr = tail.next
        prev = head 
        
        while curr:
            if not curr.next:
                prev = curr
                break

            tail.next = curr.next
            tail = tail.next

            curr.next = tail.next
            prev = curr
            curr = curr.next



        prev.next = new
        tail.next = None

        return head