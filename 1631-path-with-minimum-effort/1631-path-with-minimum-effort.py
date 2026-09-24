class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        ROWS,COLS=len(heights), len(heights[0])
        
        pq = [[0,0,0]]
        visited = set()
        delts = [[0,1],[1,0],[0,-1],[-1,0]]
        while pq:
            
            diff,r,c = heapq.heappop(pq)
            if (r,c) in visited:
                continue
            visited.add((r,c))
            
            if r==ROWS-1 and c==COLS-1:
                return diff
            
            for dr, dc in delts:
                neighborR,neighborC = r+dr, c+dc
                if (neighborR<0 or neighborC<0 or neighborR==ROWS or neighborC==COLS or (neighborR, neighborC) in visited):
                    continue
                heapq.heappush(pq, [max(diff, abs(heights[neighborR][neighborC]-heights[r][c])), neighborR,neighborC])
                    