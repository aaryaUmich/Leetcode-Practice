class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        sum = 0

        for i in range(k):
            sum+=nums[i]
        
        max_sum = sum

        for i in range(k,len(nums)):
            sum = sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, sum)
        return max_sum/k
            