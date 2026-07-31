class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = {i:[] for i in range(n)}

        for parent,child in edges:
            adj[parent].append(child)
            adj[child].append(parent)


        def dfs(node, prev):

            if node in visited:
                return False
            
            visited.add(node)
            
            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                if dfs(neighbor, node) == False:
                    return False

            return True
        

        return dfs(0,-1) and n==len(visited)
      
        
        