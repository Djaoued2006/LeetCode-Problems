# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return None

        slow , fast = None , head

        while fast:
            if fast.next:
                if not slow:
                    slow = fast
                else:
                    slow = slow.next
            
                fast = fast.next.next
            else:
                break
            
        slow.next = slow.next.next
        
        return head
