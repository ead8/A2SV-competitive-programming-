class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        srted=sorted(points,key=lambda a:(a[0])**2+(a[1]**2))
        ans=[]
        for i in range(k):
            ans.append(srted[i])

        return ans
