class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(0,len(nums)):
            diff = target-nums[i]

            if nums[i] not in map:
                map[diff] = i
            else:
                return [i, map[nums[i]]]
                
        

        
