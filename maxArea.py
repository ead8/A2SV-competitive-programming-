class Solution:
    def maxArea(self, height: List[int]) -> int:
        mxarea=area=0
        p1,p2=0,len(height)-1

        while p1<p2:
            if height[p1]<height[p2]:
                area=height[p1]*(p2-p1)
                p1+=1
            else:
                area=height[p2]*(p2-p1)
                p2-=1
            if area>mxarea:
                mxarea=area
        
        return mxarea
            



