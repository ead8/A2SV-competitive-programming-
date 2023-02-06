class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m=len(l)
        res=[True]*m
        for i in range(m):
            query=nums[l[i]:r[i]+1]
            query.sort()
          
            for j in range(1,len(query)-1):
                if query[j+1] - query[j] != query[1] - query[0]:
                    res[i]=False
                    break
               
        return res
