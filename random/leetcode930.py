class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
      
        result = 0
        curr = 0
        nlen = len(nums)

        start , end = 0 , 0

        while start < nlen:

            if end == nlen:
                start += 1
                end = start
                
            if nums[end] == 1:
                curr += 1
                if curr == goal:
                    result += 1
                    end += 1
                elif curr > goal:
                    curr -= nums[start]
                    start += 1
                    end = start
                else:
                    end += 1
            else:
                end += 1
        
        return result

