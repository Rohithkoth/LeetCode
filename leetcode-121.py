class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmin = prices[0]
        maxprof = 0
        for i in range(1,len(prices)):
            if prices[i] <= currmin:
                currmin = prices[i]
            maxprof = max(maxprof, prices[i]-currmin)
        return maxprof