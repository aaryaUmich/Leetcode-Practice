class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxP = 0
        for r in range(len(prices)):
            curr = 0
            if prices[r]>prices[l]:
                curr = prices[r]-prices[l]
                maxP = max(maxP,curr)
            else:
                l = r
        return maxP
