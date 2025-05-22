class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        if len(tokens)==1:
            return int(tokens[0])
        
        for token in tokens:
            if token != '+' and token !='-' and token !='*' and token !='/':
                stack.append(token)
            else:
                first = int(stack.pop())
                second = int(stack.pop())

                if token == '+':
                    res = first+second
                elif token == '-':
                    res = second-first
                elif token == '*':
                    res = first*second
                else:
                    res = int(second/first)
                stack.append(res)
        return res