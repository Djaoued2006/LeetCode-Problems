class ListNode:
    def __init__(self, key: int, next=None):
        self.key = key 
        self.next = next
    
class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if key not in self.set:
            self.set.append(key)
    
    def remove(self, key: int) -> None:
        if key in self.set:
            del self.set[key]
        
    def contains(self, key: int) -> bool:
        return key in self.set

def listify(head):
    curr = head 
    nodes = []
    while curr:
        nodes.append(curr.key)
        curr = curr.next
    
    return nodes 

s = MyHashSet()
result = []


def do(action, data):
    match action:
        case "add":
            s.add(data[0])
            result.append(None)
        case "remove":
            s.remove(data[0])
            result.append(None)
        case "contains":
            result.append(s.contains(data[0]))
    print(s.set) 
   
actions = ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
data = [[],[1],[2],[1],[3],[2],[2],[2],[2]]

for i in range(1,len(actions)):
    do(actions[i], data[i])

print(result)