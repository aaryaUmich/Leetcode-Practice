class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        path = []
        visited = {}
        completed = {}

        def dfs(crs):
            if crs in visited:
                return False

            if crs in completed:
                return True

            visited[crs] = 1
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            path.append(crs)
            completed[crs]=1
            del visited[crs]

        for crs in preMap:
            if dfs(crs) == False:
                return []
        return path
        