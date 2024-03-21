class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        left , right = 0 , 0

        l = len(nums)
        currSum = 0 

        while left < l:
            if right == l:
                currSum = 0
                left += 1
                if left == l:
                    break 
                right = left 
            
            currSum += nums[right]

            if currSum == goal:
                count += 1
                print(nums[left:right+1])
            else:
                if currSum > goal:
                    currSum -= nums[left]
                    left += 1
                    currSum -= nums[right]
                    right -= 1
            
            right += 1

        
        return count

nums = [0,1,1,1,1]
print(Solution().numSubarraysWithSum(nums , 3))