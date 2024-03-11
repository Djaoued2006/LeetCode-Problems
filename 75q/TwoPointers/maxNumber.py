class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums) - 1

        nums.sort()
        count = 0

        while (left < right):
            if (nums[left] + nums[right] == k):
                count += 1
                left += 1
                right -= 1
            else:
                if (nums[left] + nums[right] > k):
                    right -= 1
                else:
                    left += 1
        
        return count
            
        


            
        