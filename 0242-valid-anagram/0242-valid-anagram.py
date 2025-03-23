class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for c in s:
            if c not in countS:
                countS[c] = 1
            else:
                countS[c]+=1
        
        for c in t:
            if c not in countT:
                countT[c] = 1
            else:
                countT[c]+=1

        for i in countS.keys():
            if i not in countT or countS[i]!=countT[i]:
                return False
        
        return True
        