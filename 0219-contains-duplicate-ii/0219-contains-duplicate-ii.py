class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in indices and abs(i-indices[num])<=k:
                return True
            else:
                indices[num] = i
        return False
