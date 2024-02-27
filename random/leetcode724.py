class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        leftSum = 0
        rightSum = sum(nums[1:])

        i = 0

        while True:
            if (leftSum == rightSum):
                return i
            if (i == len(nums)-1) :
                return -1
            else :
                leftSum += nums[i]
                i += 1
                rightSum -= nums[i]

nums = [1,6,3,6,5,6]
result = Solution().pivotIndex(nums)

print(result)
