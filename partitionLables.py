class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        rightmost={}
        l,r=0,0
        partitionSize=[]
        for c in s:
            rightmost[c]=s.rindex(c)
        
        for i,c in enumerate(s):
            r=max(r,rightmost[c])

            if i==r:
                partitionSize+=[r-l+1]
                l=i+1
        return partitionSize

