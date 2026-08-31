class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""

        digits = ['1','2','3','4','5','6','7','8','9']
        

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(substring*int(k))
        
                 
                
        return "".join(stack)

            

