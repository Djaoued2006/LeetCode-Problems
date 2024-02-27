class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        length = len(height)

        left = 0
        max = 0

        while (left < length):
            right = left + 1
            diff = right - left
            while (right < length):
                amount = diff * min(height[right] , height[left])
                if (amount > max):
                    max = amount
                right += 1
            left += 1
        return max

height =  [1 , 1]
print(Solution().maxArea(height))

