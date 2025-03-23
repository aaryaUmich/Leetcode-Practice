class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        map = {}
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                if grid[i][j] not in map:
                    map[grid[i][j]] = 1
                else:
                    map[grid[i][j]] += 1
            
        final_list = []

        for i in map.keys():
            if map[i] > 1:
                final_list.append(i)
            
        for i in range(0, len(grid)*len(grid)):
            if i+1 not in map:
                final_list.append(i+1)


        return final_list
        
        