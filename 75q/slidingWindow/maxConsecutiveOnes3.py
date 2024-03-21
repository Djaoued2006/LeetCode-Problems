class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_length = 0

        number_of_flipped_zeros = 0

        left, right, length = 0 , 0 , len(nums)

        while left < length:
            if right == length:
                return max(max_length , right - left)
                
            if not nums[right]:
                if number_of_flipped_zeros == k:
                    max_length = max(max_length , right - left)

                    if not nums[left]:
                        number_of_flipped_zeros -= 1
                    
                    left += 1

                else:
                    number_of_flipped_zeros += 1
                    right += 1
            else:
                right += 1
        
        return max_length