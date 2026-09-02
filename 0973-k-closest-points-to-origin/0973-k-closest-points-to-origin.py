import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0,0]

        distances = []
        res = []

        for point in points:
            # Fixed: math.sqrt(...) and wrapped the pair in standard list brackets [...]
            distances.append([math.sqrt(((origin[0]-point[0])**2) + (origin[1]-point[1])**2), point])

        distances.sort()

        for i in range(k):
            res.append(distances[i][1])
        
        return res