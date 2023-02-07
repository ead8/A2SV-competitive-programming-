class Solution:
    def reverseParentheses(self, s: str) -> str:
        sta=[]
    
        for i,char in enumerate(s):

            if char=='(':
                sta.append(i)
            elif char==')':
                l=sta.pop()
                s=s[:l+1]+s[l+1:i+1][::-1]+s[i+1:]
     
        s=s.replace('(','').replace(')','')
        return s

