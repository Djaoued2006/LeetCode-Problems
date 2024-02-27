class Solution:
    def gcd(self , a , b : int) -> int:
        if (b == 0):
            return a
        else :
            if (a % b == 0):
                return b 
            else:
                r = a - b * (a // b)
                return Solution().gcd(b , r)
            
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 == str2 + str1):
            return str1[:Solution().gcd(len(str1) , len(str2))]
        else:
            return ''