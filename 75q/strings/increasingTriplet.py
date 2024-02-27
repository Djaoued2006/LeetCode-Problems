class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        length = len(nums)

        for i in range(length - 2):
            for j in range(i + 1 , length - 1):
                if (nums[i] < nums[j]):
                    for k in range(j + 1, length):
                        if (nums[j] < nums[k]):
                            return True
        
        return False