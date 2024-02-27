# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:

          #first solution:
#         n = len(nums)

#         count = 0

#         for i in range(len(nums)):
#             if (nums[i] == 0): count += 1
                
#         prev = 0
#         i =  prev

        

#         while (count != 0):
#             if (nums[i] == 0):
#                 prev = i
                
#                 while (i < n - 1):
#                     nums[i] , nums[i + 1] = nums[i + 1] , nums[i]
#                     i += 1
                    
#                 if (nums[prev] != 0):
#                     i = prev + 1
#                 else:
#                     i = prev
                    
#                 count -= 1
#             else:
#                 i += 1

# second solution:

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:

        n = len(nums)
        
        result = [0] * n

        j = 0

        for i in range(n):
            if (nums[i] != 0):
                result[j] = nums[i]
                j += 1
        
        for i in range(n):
            nums[i] = result[i]


#third solution:
# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         left = 0
#         n = len(nums)

#         while (left < n):
#             if (nums[left] == 0):
#                 right = left + 1

#                 while (right < n):
#                     if (nums[right] != 0):
#                         break
#                     else:
#                         right += 1
                
#                 if (right == n):
#                     break
#                 else:
#                     nums[left] , nums[right] = nums[right] , 0
            
#             left += 1

nums = [0 , 1 , 3 , 2 , 0 , 210 , 20 , 23  , 23 , 0]
Solution().moveZeroes(nums)
print(nums)