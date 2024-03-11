class Solution:
    def maxArea(self, height: list[int]) -> int:
        

        length = len(height)

        left = 0
        right = length - 1

        maxArea = 0

        while (left < right):
            area = min(height[left] , height[right]) * (right - left)
            maxArea = max(area , maxArea)

            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
