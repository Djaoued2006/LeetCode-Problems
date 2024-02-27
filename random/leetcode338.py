class Solution:

    def count0s(self , n : int) -> int :
        count = 0
        while (n != 0):
            if (n % 10 == 1):
                count += 1
            n //= 10
        
        return count


    def findBin(self , n : int) -> int:
        q = n
        result = 0
        m = 1
        
        while (q != 0):
            r = q % 2
            result = r * m + result
            m *= 10
            q //= 2
        
        return result

    def countBits(self, n: int) -> list[int]:
        result = []
        number = 0
        while (number <= n):
            result.append(Solution().count0s(Solution().findBin(number)))
            number += 1
    
        return result

number = 10121
print(Solution().countBits(number))
        