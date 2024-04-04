class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product, left, right = 1, 0 , 0
        l = len(nums)
        count = 0

        while right < l:
            if product * nums[right] >= k:
                if left == right:
                    right += 1
                else:
                    product /= nums[left]
                left += 1
            else:
                count += 1 + (right - left)
                product *= nums[right]
                right += 1
            
        return count

