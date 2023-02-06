class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        sm=0
        for t in tokens:
            if t in set(['-','+','/','*']):
                x,y=stk.pop(),stk.pop()
                if t=='+':
                    stk.append(x+y)
                elif t=='-':
                    stk.append(y-x)
                elif t=='/':
                    stk.append(int(y/x))
                elif t=='*':
                    stk.append(x*y)
            else:stk.append(int(t))
        return stk[0] 

          
