class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # dfs --> pass in r,c,target_idx
        # do bounds check, return False if out of bounds
        # check if any of the neighbors = val at target_idx
        # if so, update target_idx, and do recursive call

        # iterate through r,c --> do dfs, if a single result returns true, return true for program

        def dfs(r,c,target_idx):
            if r<0 or r>=ROWS or c<0 or c>=COLS or target_idx>=len(word):
                return False
            if board[r][c] != word[target_idx]:
                return False
            if target_idx == len(word)-1:
                return True

            original = board[r][c]
            board[r][c] = 0
            target_idx +=1
            left = dfs(r-1,c, target_idx)
            right = dfs(r+1,c, target_idx)
            up = dfs(r,c-1, target_idx)
            down = dfs(r,c+1, target_idx)
            board[r][c] = original
            return (left or right or up or down)

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False
            