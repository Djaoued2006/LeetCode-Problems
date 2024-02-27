class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        i = 0
        length = len(candies)

        while (i < length):
            candies[i] = (candies[i] - extraCandies) >= 0
            i += 1

        return candies