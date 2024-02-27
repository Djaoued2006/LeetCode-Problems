class Solution:
    def removeStars(self, s: str) -> str:

        length = len(s)

        letters = []

        i = 0

        while (i < length):
            if (s[i] == "*"):
                letters.pop()
            else :
                letters.append(s[i])
            i += 1
        
        return "".join(letters)

string = "l*code"
print(Solution().removeStars(string))

