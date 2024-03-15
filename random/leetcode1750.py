class Solution:
    def minimumLength(self, s: str) -> int:
        slen = len(s)

        left , right = 0 , slen - 1

        result = s

        while True:
            if (s[left] != s[right]):
                print(s[left] , s[right])
                return len(result)
            else:
                if (len(s) == 0):
                    return 0
                

                letter = s[left]

                while (s[left] == letter):
                    left += 1
                    if (left >= right):
                        return 0
                
                left -= 1

                if (left >= right):
                    return  0 

                while (s[right] == letter):
                    right -= 1
                    if (right <= left):
                        return 0
                
                right += 1

                if (right <= left):
                    return 0
                
                result = s[left + 1:right]
                right -= 2
                left = 0
                s = result
            
                



s = "cabaabac"
print(Solution().minimumLength(s))
        