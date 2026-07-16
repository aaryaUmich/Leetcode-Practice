class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freqs = {}

        for num in nums:
            if num in freqs:
                freqs[num]+=1
            else:
                freqs[num] = 1
        

        for i in freqs:
            if freqs[i] == 1:
                return i