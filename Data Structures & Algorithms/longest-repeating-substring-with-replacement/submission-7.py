class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
        max_freq = 0
        window = {}

        for r in range(len(s)):
            if s[r] in window:
                window[s[r]]+=1
            else:
                window[s[r]] = 1
            
            max_freq = max(window.values())

            if k>=(r-l+1) - max_freq:
                curr_max = r-l + 1
            else:
                window[s[l]]-=1
                l+=1

            max_len = max(max_len, curr_max)
            
        
        return max_len

            

        
                
