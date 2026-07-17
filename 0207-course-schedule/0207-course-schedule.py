class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            courseMap[crs].append(pre)

        visited = {}

        def dfs(crs):
            if crs in visited:
                return False

            if courseMap[crs] == []:
                return True

            visited[crs]=1
            for pre in courseMap[crs]:
                if dfs(pre) == False:
                    return False
                
            del visited[crs]
            courseMap[crs] = []
            return True

        for crs in courseMap:
            if dfs(crs) == False:
                return False
        return True
