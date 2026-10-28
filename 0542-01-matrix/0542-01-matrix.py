from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        ROWS,COLS = len(mat), len(mat[0])
        res = [[-1]*COLS for _ in range(ROWS)]
        
        dq = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    dq.append((r,c))
                    res[r][c] = 0
       
        deltas = [(1,0), (-1,0), (0,1), (0,-1)]
        while len(dq)>0:
            curr_r, curr_c = dq.popleft()
            for d in deltas:
                new_r, new_c = curr_r+d[0], curr_c+d[1]
                if new_r>=0 and new_r<ROWS and new_c>=0 and new_c<COLS:
                    if res[new_r][new_c] == -1:
                        res[new_r][new_c] = res[curr_r][curr_c]+1
                        dq.append((new_r, new_c))
        return res

        