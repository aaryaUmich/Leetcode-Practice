class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        def dfs(node, prev, visited):
            if node in visited:
                return True
            
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                
                if dfs(neighbor, node, visited):
                    return True

            return False
        

        for node,neighbor in edges:
            visited = set()
            adj[node].append(neighbor)
            adj[neighbor].append(node)
            if dfs(node, neighbor, visited):
                return [node, neighbor]

                