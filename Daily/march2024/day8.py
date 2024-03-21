#time: 45ms

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        #count frequencies

        occ = dict()    
        l = len(nums)

        for i in range(l):
            if nums[i] in occ:
                occ[nums[i]] += 1
            else:
                occ[nums[i]] = 1
            
        #getting the max frequency
        
        maxFreq = 0
        count = 0

        for key in occ:
            if occ[key] > maxFreq:
                count = 0
                maxFreq = occ[key]
            
            if maxFreq == occ[key]:
                count += maxFreq
        
        return count