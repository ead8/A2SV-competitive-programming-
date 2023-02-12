class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk=[]
        ans=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]]<temp:
                ans[stk[-1]]=i-stk[-1]
                stk.pop()
                
            stk.append(i)
        return ans
