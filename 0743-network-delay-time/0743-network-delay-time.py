from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        pq = []
        dist = [sys.maxsize]*(n+1)
        dist[k] = 0
        edges = defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))

        heapq.heappush(pq, (0, k))
        while pq:
            d, u = heapq.heappop(pq)
            if d>dist[u]:
                continue
            
            for v,w in edges[u]:
                if dist[u]+w<dist[v]:
                    dist[v] = dist[u]+w
                    heapq.heappush(pq,(dist[v], v))
        
        
        
        del dist[0]

        res = max(dist)

        if res == sys.maxsize:
            return -1
        return res
            