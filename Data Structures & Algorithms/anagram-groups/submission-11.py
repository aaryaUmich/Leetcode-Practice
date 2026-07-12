
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            
            freq = [0]*26
            for l in range(len(s)):
                freq[ord(s[l]) - ord('a')]+=1
            
            group[tuple(freq)].append(s)
        

        return list(group.values())
