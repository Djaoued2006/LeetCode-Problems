class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if (n == 0):
            return True
        else:
            length = len(flowerbed)
            count = 0

            if (length >= 2):
                if ((flowerbed[0] == 0) and (flowerbed[1] == 0)):
                    flowerbed[0] = 1
                    count += 1
                    if (count == n): 
                        return True
                
            
            if ((flowerbed[length - 1] == 0) and (flowerbed[length - 2] == 0)):
                    flowerbed[length - 1] = 1
                    count += 1
                    if (count == n):
                        return True
            
            for i in range(1 , length - 1):
                if ((flowerbed[i] == 0) and (flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0)):
                    flowerbed[i] = 1
                    count += 1
                    if (count == n):
                        return True
        
        
                 