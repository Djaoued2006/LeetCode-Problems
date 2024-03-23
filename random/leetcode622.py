#leetcode problem : 622. Design Circular Queue

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = -1
        self.back = -1
        self.queue = [0] * k
        self.size = 0
        self.maxSize = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.back == -1:
            self.front = 0
            self.back = 0
        else:
            self.back = (self.back + 1) % self.maxSize
        
        self.queue[self.back] = value
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.maxSize
        self.size -= 1

        if self.isEmpty():
            self.front = -1
            self.back = -1
            
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.back]

    def isEmpty(self) -> bool:
        return not self.size
        

    def isFull(self) -> bool:
        return self.size == self.maxSize


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()