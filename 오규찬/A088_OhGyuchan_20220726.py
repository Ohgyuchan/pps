class MinStack:

    def __init__(self):
        self.a = []
        self.ma = []
        

    def push(self, val: int) -> None:
        self.a.append(val)
        
        if len(self.ma) == 0:
            self.ma.append(val)
        else:
            self.ma.append(min(val, self.ma[-1]))
        

    def pop(self) -> None:        
        self.ma.pop()
        return self.a.pop()
        

    def top(self) -> int:
        return self.a[-1]
        

    def getMin(self) -> int:
        return self.ma[-1]