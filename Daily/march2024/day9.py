#time : 335ms 
#leetcode problem : 2540. Minimum Common Value

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        p1 , p2 = 0 , 0 
        l1 , l2 = len(nums1) , len(nums2)

        while True:
            if p1 == l1 or p2 == l2:
                return -1

            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            
            if nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        
            

        