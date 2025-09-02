class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recurrence relation: T(i,j) = T(i-1,j)+T(i,j-1)
        memo = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        for row in range(1,m):
            for col in range(1,n):
                memo[row][col] = memo[row-1][col]+memo[row][col-1]
        
        return memo[m-1][n-1]
