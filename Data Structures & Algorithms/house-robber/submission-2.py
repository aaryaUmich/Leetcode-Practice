class Solution:
    def rob(self, nums: List[int]) -> int:
        #memo[i] represents max amnt of money we could rob up until i
        if len(nums)==1:
            return nums[0]
        
        memo = [nums[0],max(nums[0], nums[1])]

        def dfs(n):
            for i in range(2,n):
                memo.append(max(nums[i]+memo[i-2], memo[i-1]))
            
            return memo[n-1]
        
        return dfs(len(nums))