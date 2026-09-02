class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store (squared_distance, point) tuples
        distances = [(p[0]**2 + p[1]**2, p) for p in points]
        
        # Sort by squared distance ascending
        distances.sort()
        
        # Return the original point coordinates for the top k elements
        return [point for dist, point in distances[:k]]