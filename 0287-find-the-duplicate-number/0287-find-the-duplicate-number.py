class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        first = 0
        second = 0
        for first in range(0,len(nums)-1):
            second = first+1
            if nums[first] == nums[second]:
                return nums[second]
        return nums[second]
