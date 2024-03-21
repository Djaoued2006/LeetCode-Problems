class Solution:
    def minimumLength(self, s: str) -> int:
       
        while s:
            left , right = 0 , len(s) - 1
            
            if s[left] != s[right] or left == right:
                break 
            
            prefix = s[left]
            suffix = s[right]

            while prefix == s[left]:
                if left == right:
                    break
                left += 1

            left -= 1   

            while suffix == s[right]:
                if left == right:
                    break 
                right -= 1
            
            right += 1
        
            s = s[left+1:right] 

        return len(s)