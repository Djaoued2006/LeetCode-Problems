from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNones(self , lists : list[Optional[ListNode]]) -> list[Optional[ListNode]]:
        
        i = 0
        l = len(lists)

        while (i < l):
            if not lists[i]:
                del lists[i]
                l -= 1
            else:
                i += 1 

        return lists
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        last = None
        nodes = [lists[i] for i in range(len(lists))]

        while True:
            
            lists = self.deleteNones(lists)
            
            l = len(lists)
            
            if not l:
                break

            currentValues = [lists[i].val for i in range(l)]
            
            index = 0
            minValue = 10 ** 4 + 1
            for i in range(l):
                if currentValues[i] < minValue:
                    index = i 
                    minValue = currentValues[i]
            
            temp = lists[index].next
            lists[index].next = None

            if not result:
                result = lists[index]
                last = result
            else:
                last.next = lists[index]
                last = lists[index]
            
            lists[index] = temp
        
        return result


