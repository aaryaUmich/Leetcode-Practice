class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        dist = [sys.maxsize]*n
        dist[src] = 0
        for i in range(k+1):
            new_dist = dist.copy()
            for u,v,w in flights:
                if dist[u] != sys.maxsize and dist[u]+w<new_dist[v]:
                    new_dist[v] = dist[u]+w
        
            dist = new_dist
        
        
        res = dist[dst]

        if res == sys.maxsize:
            return -1
        return res

        




