class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_freq = {}
        s2_freq = {}
        
        if len(s1)>len(s2):
            return False

        for s in s1:
            if s in s1_freq:
                s1_freq[s]+=1
            else:
                s1_freq[s] = 1
        
        for r in range(len(s2)):
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1

            if (r-l+1)>len(s1):
                s2_freq[s2[l]]-=1
                if s2_freq[s2[l]]==0:
                    del s2_freq[s2[l]]
                l+=1
            

            if s1_freq == s2_freq:
                return True
        return False

