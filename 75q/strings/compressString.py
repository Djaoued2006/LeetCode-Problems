class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        n = len(chars)
        i = 0

        while (i < n):
            value = chars[i]
            count = 0

            for j in range(i , n):
                if (chars[j] != value):
                    break
                else:
                    count += 1
            
            if (count == 1):
                s += value
            else:
                s += value + str(count)
            
            if (j == i):
                i += 1  
            elif (j != n - 1):
                i = j
            else:
                i = n
        
        chars = list(s)
        print(chars)

        return len(chars)

s = 'djaaoueed'
chars = ["a","a","b","b","c","c","c"]
print(Solution().compress(chars))