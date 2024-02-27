class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        
        for i in range(len(candies)):
            candies[i] = (candies[i] + extraCandies >= maxCandies)
        
        return candies