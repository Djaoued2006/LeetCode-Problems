class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        countZeros = 0
        result = 0

        left = 0
        right = 0
        n = len(nums)

        while (right != n):
            if (nums[right] == 0):
                if (countZeros == k):
                    left += 1
                    result = max(result , (right - left))
                else:
                    countZeros += 1
            right += 1
        
        result = max(result , (right - left))
        
        return result

nums = [1 , 0 , 0 , 1]
k = 2
print(Solution().longestOnes(nums , k))
