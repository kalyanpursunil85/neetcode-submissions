class MinStack:

    def __init__(self):
        self.l = []
        

    def push(self, val: int) -> None:
        min_val = min(self.l[-1][0], val) if self.l else val
        self.l.append((min_val, val))
        

    def pop(self) -> None:
        del self.l[-1]
        

    def top(self) -> int:
        return self.l[-1][1]
        

    def getMin(self) -> int:
        return self.l[-1][0]

        
