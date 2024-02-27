class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sptr = 0
        tptr = 0

        slen = len(s)
        tlen = len(t)

        while ((sptr < slen) and (tptr < tlen)):
            if (s[sptr] == t[tptr]):
                sptr += 1
            
            tptr += 1
        
        return (sptr == slen)

s = 'ace'
t = 'djaoued'

print(Solution().isSubsequence(s , t))

