class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        slen = len(s)

        result = [""] * slen
        left, right = 0 , slen - 1

        for i in range(slen):
            if (s[i] == "1"):
                result[left] = s[i]
                left += 1
            else:
                result[right] = s[i]
                right -= 1
        
        result[right] = "0"
        result[slen - 1] = "1"

        return "".join(result)
            


                
s = "01001110"

print(Solution().maximumOddBinaryNumber(s))