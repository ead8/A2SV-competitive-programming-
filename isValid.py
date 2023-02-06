class Solution:
        
    def isValid(self, s: str) -> bool:
        left='({['
        right=')}]'
        stack=[]
        match=False
        if len(s)%2!=0:
            return False
        for el in s:
            if el in left:
                stack.append(el)
            else:
                if len(stack)!=0:
                    topEl=stack.pop()
                    if left.index(topEl)==right.index(el):
                        match=True
                    else: return False
                    # print(topEl,el)
                else:return False
        return match if len(stack)==0 else False
