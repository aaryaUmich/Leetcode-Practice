class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0

        min_len = 1000000
        total = 0

        for r in range(len(nums)):
            total += nums[r]

            while total>=target:
                min_len = min(min_len, r-l+1)
                total-=nums[l]
                l+=1
            
        
        if sum(nums)<target:
            return 0
        
        else:
            return min_len
        
