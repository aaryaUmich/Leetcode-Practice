class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')', '{':'}', '[':']'}

        
        stack = [] 

        for i in range(0,len(s)):
            
            if s[i] in mapping:
                stack.append(s[i])

            elif len(stack)==0:
                return False
            
            elif s[i] == mapping[stack[-1]]:
                stack.pop()
            
            else:
                return False


        
        return len(stack)==0 