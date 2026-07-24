class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num]+=1
        


        freqs_sorted = []


        for num in freqs:
            freqs_sorted.append((freqs[num], num))
        


        freqs_sorted.sort(reverse=True)

        res = []

        for i in range(0,k):
            res.append(freqs_sorted[i][1])
        
        return res