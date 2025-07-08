class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        l,maxL = 0,0

        for r in range(len(s)):
            freqs[s[r]] = 1+ freqs.get(s[r], 0) 
            
            while (r-l+1) - max(freqs.values()) > k:
                freqs[s[l]]-=1
                l+=1

            maxL = max(maxL, r-l+1)

        return maxL

        