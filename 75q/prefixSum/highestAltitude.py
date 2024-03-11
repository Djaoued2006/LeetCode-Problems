class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        n = len(gain)
        alt = [0] * (n + 1)

        for i in range(n):
            alt[i + 1] = alt[i] + gain[i]
        
        return max(alt)

gain = [-4,-3,-2,-1,4,3,2]
print(Solution().largestAltitude(gain))
    