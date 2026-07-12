class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_len = 0
        freq = {}
        if len(s)==0:
            return 0
        
        for r in range(len(s)):
            while s[r] in freq:
                del freq[s[l]]
                l+=1
            freq[s[r]] = 1
            max_len = max(max_len, r-l)        
        
        return (max_len+1)