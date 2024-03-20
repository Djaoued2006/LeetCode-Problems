class Solution:
    def compress(self, chars: list[str]) -> int:

        s = ""
        i = 0
        clen = len(chars)

        while i < clen:
            letter = chars[i]
            j = i + 1

            while j < clen:
                if chars[j] != letter:
                    break 
                else:
                    j += 1
            
            count = j - i

            if count == 1:
                s += chars[i]
            else:
                count = str(count)
                s += chars[i] + count 
            
            i = j 

        length = len(s)      
        chars[:] = list(s)

        return length


s = 'djaaoueed'
chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))
print(chars)
