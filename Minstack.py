class MinStack:

    def __init__(self):
        self.stk1 = []
        self.minstk = []

    def push(self, val: int) -> None:
        if len(self.minstk)==0 or val<=self.minstk[-1]:
            self.minstk.append(val)
        
        self.stk1.append(val)
    
        print(self.minstk)
    def pop(self) -> None:
        if self.minstk[-1]==self.stk1[-1]:
            self.minstk.pop()
        self.stk1=self.stk1[:-1]
        

    def top(self) -> int:
        return self.stk1[-1]
        

    def getMin(self) -> int:
        return self.minstk[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
