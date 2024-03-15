class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        numsLen = len(nums)

        for i in range(numsLen):
            nums[i] = nums[i] ** 2
        
        return sorted(nums)
    
        