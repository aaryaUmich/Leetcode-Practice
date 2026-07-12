class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr_window = {}
        max_len = 0

        if len(s)==0:
            return 0
        
        for r in range(len(s)):
            while s[r] in curr_window:
                del curr_window[s[l]]
                l+=1
            curr_window[s[r]] = 1
            max_len = max(max_len, len(curr_window.keys()))
        
        return max_len
