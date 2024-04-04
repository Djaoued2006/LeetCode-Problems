class Object:
    def __init__(self, key, value):
        self.key = key 
        self.value = value 

class ListNode:
    def __init__(self, obj: Object, next=None):
        self.obj = obj 
        self.next = next
        self.times = 0

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currSize = 0
        self.data = None 
        self.keys = dict()

    def get(self, key: int):
        if key in self.keys:
            self.keys[key].times += 1
            return self.keys[key].obj.value 
        
        return -1


    def put(self, key: int, value: int):
        obj = Object(key, value)
        
        if self.currSize == self.capacity:
            curr = self.data
            minTimesVisited = float("inf")
            
            while curr:
                if curr.times < minTimesVisited:
                    node = curr 
                    minTimesVisited = curr.times 
                    if not minTimesVisited:
                        break 
                curr = curr.next

            self.keys.pop(node.obj.key, 'nothing')
            node.obj = obj 
        else:
            node = ListNode(obj)
            node.next = self.data 
            self.data = node
            self.currSize += 1

        self.keys[key] = node  
 

actions = ["LRUCache","put","put","get","put","get","put","get","get","get"]
data = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

returns = []

def do(action, data):
    global cache
    
    match action:
        case "LRUCache":
            cache = LRUCache(data[0])
            returns.append(None)
        case "put":
            cache.put(data[0], data[1])
            returns.append(None)
        case "get":
            returns.append(cache.get(data[0]))
    

for i in range(len(actions)):
    do(actions[i] , data[i])

print(returns)
print(len(actions) == len(returns))