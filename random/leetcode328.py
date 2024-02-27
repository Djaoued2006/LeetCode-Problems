from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def convertLinkedListToArray(self , head) -> list[int] :

        result = []
        currentNode = head 

        while (currentNode != None):
            result.append(currentNode.val)
            currentNode = currentNode.next 
        
        return result

    def convertArrayToLinkedList(self , nums : list[int]) :


        head = ListNode(nums[0])
        currentNode = head
        length = len(nums)
        i = 1

        while (i < length):
            newNode = ListNode(nums[i])
            currentNode.next = newNode
            currentNode = newNode 
            i += 1
        
        return head

    def printLinkedList(self , head):

        currentNode = head 

        while (currentNode.next != None):
            print(currentNode.val , end=" -> ")
            currentNode = currentNode.next 
        
        print(currentNode.val)




class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nums = ListNode().convertLinkedListToArray(head)
        length = len(nums)

        i = 2

        newHead = ListNode(nums[0])
        currentNode = newHead

        while (i < length):
            newNode = ListNode(nums[i])
            currentNode.next = newNode
            currentNode = newNode
            i += 2
        
        i = 1

        while (i < length):
            newNode = ListNode(nums[i])
            currentNode.next = newNode 
            currentNode = newNode
            i += 2
        
        return newHead

nums = [1 , 2 , 3 , 4 , 5]

head = ListNode().convertArrayToLinkedList(nums)

head = Solution().oddEvenList(head)

print(head.val)

ListNode().printLinkedList(head)



