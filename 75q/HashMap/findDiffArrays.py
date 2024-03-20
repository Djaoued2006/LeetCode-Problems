class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        inNums1 = dict()
        inNums2 = dict()

        n1len = len(nums1)
        n2len = len(nums2)

        for i in range(min(n1len , n2len)):
            inNums1[nums1[i]] = True 
            inNums2[nums2[i]] = True
        
        for i in range(min(n1len , n2len) , n1len):
            inNums1[nums1[i]] = True 
        
        for i in range(min(n1len , n2len) , n2len):
            inNums2[nums2[i]] = True
        
        for i in range(n1len):
            inNums2[nums1[i]] = False
        
        for i in range(n2len):
            inNums1[nums2[i]] = False

        
        result = [[] , []]
        for key in inNums1:
            value = inNums1[key]
            if value:
                result[0].append(key)
        
        for key in inNums2:
            value = inNums2[key]
            if value:
                result[1].append(key)
            
        return result