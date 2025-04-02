class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for char in magazine:
            if char not in map:
                map[char]=1
            else:
                map[char]+=1
        
        for char in ransomNote:
            if char not in map or map[char]==0:
                return False
            else:
                map[char]-=1
        
        return True