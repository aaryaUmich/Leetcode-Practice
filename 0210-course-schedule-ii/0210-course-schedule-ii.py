class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i:[] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = {}
        completed = {} #why
        res = []


        def dfs(crs):

            if crs in visited:
                return False

            if crs in completed:
                return True
            
            visited[crs] = 1
            
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            completed[crs] = 1
            del visited[crs]
            res.append(crs)
            return True
        
        for crs in preMap:
            if dfs(crs) == False:
                return []
        
        return res
        

            

        