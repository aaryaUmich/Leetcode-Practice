class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bottom = 0, rows-1

        while top<=bottom:
            middleRow = (top+bottom)//2

            if target>matrix[middleRow][-1]:
                top = middleRow+1
            
            elif target<matrix[middleRow][0]:
                bottom = middleRow-1

            else:
                break
        
        if not (top<=bottom):
            return False

        rowToSearch = (top+bottom)//2

        l,r = 0, cols-1

        while l<=r:
            middle = l+(r-l)//2

            if target > matrix[rowToSearch][middle]:
                l = middle+1
            
            elif target < matrix[rowToSearch][middle]:
                r = middle-1
            
            else:
                return True
        
        return False
            