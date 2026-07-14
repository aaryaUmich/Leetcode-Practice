class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r > height-1 or c > length-1:
                return
            
            if grid[r][c] == "1":
                grid[r][c] = "0"
                dfs(r-1,c)
                dfs(r+1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        
        length = len(grid[0])
        height = len(grid)
        counter = 0
        for i in range(height):
            for j in range(length):
                if grid[i][j]=="1":
                    counter+=1
                    #do dfs
                    dfs(i,j)
        return counter

        

            
        


