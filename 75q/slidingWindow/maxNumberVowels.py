class Solution:

    def checkVowel(self, c : str) -> bool:

        vowels = 'aeiou'
        
        return (c in vowels)
        
    def maxVowels(self, s: str, k: int) -> int:
        
        Sol = Solution()

        maxVowel = currVowel = Sol.countVowels(s[:k])
        length = len(s)

        for i in range(1 , length - k + 1):
            if Sol.checkVowel(s[i + k - 1]):
                currVowel += 1

            if (Sol.checkVowel(s[i - 1])):
                currVowel -= 1

            maxVowel = max(maxVowel , currVowel)
        
        return maxVowel