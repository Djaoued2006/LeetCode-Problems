class Solution:
    def getWords(self , s : str) -> list[str]:
        
        s += ' '
        words = []
        temp = ''

        for i in range(len(s)):
            if (s[i] != ' '):
                temp += s[i]
            else:
                if (temp != ''):
                    words.append(temp)
                temp = ''
        
        return words


    def reverseWords(self, s: str) -> str:
        arr = Solution().getWords(s)
        arr.reverse()
        return " ".join(arr)

s = "    the sky is    blue    "
print(Solution().reverseWords(s))
        