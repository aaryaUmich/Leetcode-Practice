class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]

        if og==color:
            return image
        
        def dfs(sr, sc):
            if sr>= len(image) or sc >= len(image[0]) or sr<0 or sc<0:
                return
            
            if image[sr][sc] != og:
                return


            image[sr][sc] = color
            
            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)
        
        dfs(sr, sc)
        return image
        

            
