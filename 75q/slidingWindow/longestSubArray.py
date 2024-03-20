class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        nlen = len(nums)
        left , right = 0 , 0


        #this will tell if we already deleted a zero!
        deleted = False

        maxlen = 0

        #this will tell the index of the last encountered zero
        lastZero = -1

        while left < nlen:

            if right == nlen:
                right -= 1
                maxlen = max(maxlen , right - left)
                break

            if nums[right]:
                right += 1
            else:
                if deleted:
                    maxlen = max(maxlen , right - left - 1)
                    left += 1
                    deleted = left <= lastZero  
                else:
                    deleted = True
                    lastZero = right 
                    right += 1
        
    
        return maxlen 



