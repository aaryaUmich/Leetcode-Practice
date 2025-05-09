class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        freqArray = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            if i not in map:
                map[i] = 1
            else:
                map[i]+=1
        
        for n,c in map.items():
            freqArray[c].append(n)

        
        res = []
        for i in range(len(freqArray)-1, 0, -1):
            for n in freqArray[i]:
                res.append(n)
                if len(res) == k:
                    return res


