class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        numbers = dict()
        min = 1

        for num in nums:
            if num > 0:
                numbers[num] = True 
        
        while True:
            if min in numbers:
                min += 1
            else:
                return min