from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        mins = 0
        fresh = 0
        
        def addFruit(r,c):
            nonlocal fresh
            if (r<0 or r==row or c<0 or c==col or grid[r][c]!=1):
                return
            
            grid[r][c] = 2
            fresh-=1
            queue.append([r,c])

        row, col = len(grid), len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append([r,c])
                elif grid[r][c]==1:
                    fresh+=1
        

        while queue and fresh>0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                addFruit(r+1,c)
                addFruit(r-1,c)
                addFruit(r,c-1)
                addFruit(r,c+1)
            mins+=1
        
        if fresh>0:
            return -1
        return mins







            
