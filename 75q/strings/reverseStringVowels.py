class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'

        temp = ''
        result = ''

        for i in range(len(s)):
            if (s[i] in vowels):
                temp += s[i]
        
        k = len(temp) - 1

        for i in range(len(s)):
            if (s[i] in vowels):
                result += temp[k]
                k -= 1
            else:
                result += s[i]
        
        return result
                
str1 = "hello"
print(Solution().reverseVowels(str1))