class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        i , j = 0 , 0
        nlen = len(nums)
        numberFlippedZeros = 0
        maxOnes = 0

        while i < nlen:
            # print(nums[i : j + 1])
            if nums[j] == 0:
                if numberFlippedZeros == k:
                    maxOnes = max(maxOnes , j - i)
            

                    numberFlippedZeros = 0
                    i += 1
                    j = i

                else:
                    j += 1
                    numberFlippedZeros += 1
            else:
                j += 1
            
            if j == nlen:
                maxOnes = max(maxOnes , j - i)
                i += 1
                j = i 
            
        
        return maxOnes

nums = [0,0,0,1]; k = 4
print(Solution().longestOnes(nums , k))
                