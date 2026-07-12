class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        curr_max = 0

        while l<r:
            curr_area = min(heights[l],heights[r]) * (r-l)
            if heights[l] < heights[r]:
                l+=1
            elif heights[l] >= heights[r]:
                r-=1
            curr_max = max(curr_max, curr_area)
        
        return curr_max