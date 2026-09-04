class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        curr = []
        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total>target or i==len(candidates):
                return
            
            #include elment at i
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])
            curr.pop()

            #skip elment at i
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            
            dfs(i+1, curr, total)
            
        dfs(0, curr, 0)
        return res
            

     