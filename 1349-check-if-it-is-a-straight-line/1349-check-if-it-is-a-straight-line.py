class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<2:
            return False

        if len(coordinates)==2:
            return True

        for i in range(len(coordinates)-1):
            y2 = coordinates[i+1][1] - coordinates[i][1]
            y1 = coordinates[i][1] - coordinates[i-1][1]
            x2 = coordinates[i+1][0] - coordinates[i][0]
            x1 = coordinates[i][0] - coordinates[i-1][0]
            if (y2*x1 != y1*x2):
                return False
        return True 
        