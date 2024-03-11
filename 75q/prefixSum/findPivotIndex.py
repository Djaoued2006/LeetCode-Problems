class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum , rightSum = 0 , 0
        n = len(nums)

        for i in range(1 , n):
            rightSum += nums[i]
        
        if (leftSum == rightSum):
            return 0
        
        for i in range(1 , n):
            leftSum += nums[i - 1]
            rightSum -= nums[i]
            if (leftSum == rightSum):
                return i 

        return  -1