class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #memo[i] represents minimum num of coins needed to sum to i
        memo = [9999999999999999999] * (amount+1)
        memo[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    memo[a] = min(memo[a], 1+memo[a-c])
        
        if memo[amount]==9999999999999999999:
            return -1
        
        return memo[amount]


        
