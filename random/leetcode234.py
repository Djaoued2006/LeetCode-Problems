from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head : Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     len =  0
    #     curr = head

    #     while curr:
    #         len += 1
    #         curr = curr.next

    #     if ((len == 0) or (len == 1)):
    #         return True
        
    #     curr = head
    #     for i in range(len // 2 - 1):
    #         curr = curr.next
        
    #     list = curr.next
    #     curr.next = None

    #     list = Solution().reverseList(list)
        
    #     curr = head
    #     curr2 = list

    #     while curr:
    #         if (curr.val != curr2.val):
    #             return False
    #         else:
    #             curr = curr.next
    #             curr2 = curr2.next
        
    #     return True

    def length(self , head : Optional[ListNode]) -> int :
        result = 0
        curr = head

        while curr:
            result += 1
            curr = curr.next
        
        return result

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        len = Solution.length(head)
        nodes = [None] * len

        node = head
        i = 0

        while node:
            nodes[i] = node
            node = node.next
            i += 1
        
        left , right = 0 , len - 1

        while left < right:
            if (nodes[left].val != nodes[right].val):
                return False
            
            left += 1
            right -= 1
        
        return True


        

        