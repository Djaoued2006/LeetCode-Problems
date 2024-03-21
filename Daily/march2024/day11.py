#time : 38ms
#leetcode problem : 791. Custom Sort String

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""

        for c in order:
            numberOcc = len([_ for _ in s if _ == c])
            print(c, numberOcc)
            result += c * numberOcc
    
        for c in s:
            if c not in order:
                result += c

                
        return result

order = "exv"
s = "xwvee"
print(Solution().customSortString(order , s))