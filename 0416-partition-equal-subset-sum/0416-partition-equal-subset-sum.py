class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        #memo [i][s] --> bool for if we could create sum s via the first i elements
        target = sum(nums)//2
        memo = []

        if sum(nums) % 2 != 0:
            return False

        for r in range(len(nums)+1):
            row = []
            for c in range(target+1):
                row.append(False)
            memo.append(row)

        memo[0][0] = True
        

        #recurrence relation --> memo[i][s] = memo[i-1][s] or memo[i-1][s-nums[i-1]]

        for i in range(1,len(nums)+1):
            for s in range(target+1):
                if s >= nums[i-1]:
                    memo[i][s] = memo[i-1][s] or memo[i-1][s - nums[i-1]]
                else:
                    memo[i][s] = memo[i-1][s]

        r,c = len(memo), len(memo[0])
        return memo[r-1][c-1]