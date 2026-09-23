class Solution:
    def climbStairs(self, n: int) -> int:
        #memo[i] = number of ways to climb i steps
        memo = [1,2]

        #recurrence relation memo[i]
        def dp(n):
            for i in range(2,n):
                memo.append(memo[i-2]+memo[i-1])
            
            return memo[n-1]
        
        return dp(n)