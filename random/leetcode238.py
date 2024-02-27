class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        
        length = len(nums)
        if length >= 3 : 
            i = 0
            while i < length - 2:
                j = i + 1
                while nums[j] <= nums[i] :
                    if j != length - 2:
                        j += 1
                    else :
                        i += 1
                        break
                else :
                    k = j + 1
                    while nums[k] <= nums[j] :
                        if k != length - 1:
                            k += 1
                        else :
                            j += 1
                            break
                    else :
                        return True
                
        return False

                            
