class Solution:        
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        maxSum = currSum = sum(nums[:k])
        length = len(nums)

        for i in range(1 , length - k + 1):
            currSum += nums[i + k - 1] - nums[i - 1]
            if (currSum > maxSum):
                maxSum = currSum
            
        
        return maxSum / k


c = Solution()
nums = [1,12,-5,-6,50,3]
k = 4
print(c.findMaxAverage(nums , k))        