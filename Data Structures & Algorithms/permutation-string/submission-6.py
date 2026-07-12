class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_freq = {}
        s2_freq = {}
        
        if len(s1)>len(s2):
            return False

        for i in range(len(s1)):
            s1_freq[s1[i]] = s1_freq.get(s1[i], 0) + 1
            s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1

        for r in range(len(s1), len(s2)):
            if s1_freq == s2_freq:
                return True
            
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1
            s2_freq[s2[l]]-=1
            if s2_freq[s2[l]] == 0:
                del s2_freq[s2[l]]
            l+=1
        return s1_freq == s2_freq
        
        

