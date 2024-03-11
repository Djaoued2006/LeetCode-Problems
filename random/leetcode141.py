class node:
    def __init__(self , value):
        self.value = value
        self.next = None
        return self 

class Solution:
    def hasCycle(self, head : node) -> bool:
        nodes = dict()
        
        if (head == None):
            return False
        else:
            node = head
            
            while True:
                if (node.next == None):
                    return False
                else:
                    if (node.next in nodes):
                        return True
                    else:
                        nodes[node] = True
                        node = node.next
