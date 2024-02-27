class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        
        i = 0
        result = ''

        while ((i < len1) and (i < len2)):
            result += word1[i]
            result += word2[i]
            i += 1
        
        while (i < len1):
            result += word1[i]
            i += 1
        
        while (i < len2):
            result += word2[i]
            i += 1

        return result
