from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = set()
        num = 0
        for node,neighbor in edges:
            adj[node].append(neighbor)
            adj[neighbor].append(node)

        def dfs(node, prev):
            if node in visited:
                return
            
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                
                dfs(neighbor, node)
            
        for i in range(n):
            if i not in visited:
                num+=1
                dfs(i,-1)

        return num