class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        left = 1
        right = 1

        answer = [1] * length

        for i in range(1 , length):
            answer[length - i] = right
            right *= nums[length - i]
        
        answer[0] = right 

        for i  in range(0 , length):
            answer[i] *= left
            left *= nums[i]
        
        return answer