class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = {}
        def dfs(crs):
            if crs in visited:
                return False
            
            if preMap[crs] == []:
                return True

            
            visited[crs] = 1
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False

            del visited[crs]
            preMap[crs] = []
            return True

        for crs in preMap:
            if not dfs(crs):
                return False
        return True
        