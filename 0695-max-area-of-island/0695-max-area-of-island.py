class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        length = len(grid[0])
        height = len(grid)
        max_area = 0
        curr_val = 0
        
        def dfs(r,c):
            if r<0 or c<0 or r>=height or c>=length:
                return 0
            
            if grid[r][c] == 0:
                return 0
            
            else:
                grid[r][c] = 0
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        
        for i in range(height):
            for j in range(length):
                if grid[i][j]==1:
                    curr_val = dfs(i,j)
                max_area = max(max_area, curr_val)
        
        return max_area

