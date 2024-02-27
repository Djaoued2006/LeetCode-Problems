class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i , j = 0 , 0

        # i will go all over s 

        if (s == "") or (s == t) :
            return True
        else:
            while (j < len(t)):
                if (s[i] == t[j]):
                    i += 1
                j += 1

                if (i == len(s)):
                    break

            return (i == len(s))

s = ""
t = "jdaoued"
print(Solution().isSubsequence(s , t))



