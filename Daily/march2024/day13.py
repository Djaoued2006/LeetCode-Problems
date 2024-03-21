#time: 38ms
#leetcode problem: 2485. Find the Pivot Integer

import math 

class Solution:
    def pivotInteger(self, n: int) -> int:
        value = math.sqrt((n ** 2 + n) // 2)
        if value == value // 1:
            return math.floor(value)
        else:
            return -1
        