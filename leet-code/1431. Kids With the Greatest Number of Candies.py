class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCan = max(candies)
        result = []

        for i in candies:
            if i + extraCandies >= maxCan:
                result.append(True)
            else:
                result.append(False)

        return result
