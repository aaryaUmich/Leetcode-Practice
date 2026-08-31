class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        max_water = -9999999999999999999999999999999999
        while l<r:
            curr = min(heights[l],heights[r]) * (r-l)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
            max_water = max(max_water, curr)
        
        return max_water

