class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific,atlantic = set(), set()
        
        res = []


        def dfs(r,c, visit, prev_height):
            if (r,c) in visit or r== ROWS or c== COLS or r<0 or c<0 or prev_height>heights[r][c]:
                return
            
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])  

        for c in range(COLS):
            dfs(0,c,pacific, heights[0][c])
            dfs(ROWS-1,c,atlantic,heights[ROWS-1][c])
        
        
        for r in range(ROWS):
            dfs(r,0, pacific, heights[r][0])
            dfs(r,COLS-1, atlantic, heights[r][COLS-1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append(list((r,c)))
        
        return res

            
         
            

            