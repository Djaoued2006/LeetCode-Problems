#leetcode problem: 707. Design Linked List
#time: 97ms, beats: 86.79%

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        

    def get(self, index: int) -> int:
        if index >= self.len:
            return -1

        curr = self.head

        if not curr:
            return -1
        
        while index:
            curr = curr.next 
            index -= 1
        
        return curr.value     

    def addAtHead(self, val: int) -> None:
        
        self.len += 1
        node = Node(val)
        node.next = self.head 
        
        if not self.head:
            self.tail = node 
        
        self.head = node 



    def addAtTail(self, val: int) -> None:
        
        self.len += 1

        node = Node(val)
        
        if not self.tail:
            self.head = node 
        else: 
            self.tail.next = node
        
        self.tail = node 

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.len:
            return 
                
        if not index:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        else:
            node = Node(val)
            index -= 1
            self.len += 1
            
            curr = self.head 
            
            while index:
                curr = curr.next
                index -= 1
            
            node.next = curr.next
            curr.next = node

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.len:
            return 

        self.len -= 1

        if not index:
            self.head = self.head.next
            if not self.head:
                self.tail = None 
        else:
            curr = self.head 
            index -= 1
            
            while index:
                curr = curr.next
                index -= 1
            
            if curr.next == self.tail:
                self.tail = curr
            

            curr.next = curr.next.next




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)