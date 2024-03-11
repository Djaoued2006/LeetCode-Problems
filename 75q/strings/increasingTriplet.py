class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        length = len(nums)

        first , second = float('inf') , float('inf')

        for i in range(length):
            if (nums[i] < first):
                first = nums[i]
            elif (nums[i] < second) :
                second = nums[i]
            else:
                return True

        
        return False