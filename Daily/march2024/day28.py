class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        left, right = 0, 0
        maxLength = 0
        freq = dict()
        n = len(nums)


        while right < n:
            if nums[right] in freq:
                freq[nums[right]] += 1
                if freq[nums[right]] > k:
                    maxLength = max(maxLength, right - left)
                    
                    while left < n:
                        if nums[left] != nums[right]:
                            freq[nums[left]] -= 1
                            left += 1
                        else:
                            freq[nums[left]] -= 1
                            left += 1
                            break
            else:
                freq[nums[right]] = 1
            
            right += 1
        
        return max(maxLength, right - left)
                     