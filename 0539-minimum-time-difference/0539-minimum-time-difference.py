import math
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times = []
        for timestamp in timePoints:
            hours, minutes = map(int, timestamp.split(':'))
            total_minutes = hours * 60 + minutes
            times.append(total_minutes)
        
        times.sort()

        min_diff = abs(1440-times[len(times)-1]+times[0])
        

        for i in range(len(times)-1):
            curr_diff = abs(times[i]-times[i+1])

            min_diff = min(curr_diff, min_diff)
        
        return min_diff
        







