class MinStack:

    def __init__(self):
       self.stack = [] 
       self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.min_val)
        
