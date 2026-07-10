class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l,r = 0,1

        while r<len(prices):
            curr_prof = prices[r]-prices[l]
            if prices[l]>prices[r]:
                l = r
            
            profit = max(profit, curr_prof)
            r+=1
        
        return profit