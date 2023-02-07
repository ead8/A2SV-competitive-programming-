class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<2:return 0
        lrm=mnt=0
        l=r=0
        lsub,rsub=0,len(arr)-1
        while l<=r:
            if arr[l]>=arr[l+1]:
                lsub-=1
            else:lsub+=1
            if arr[r]>=arr[r-1]:
                rsub-=1
            else:rsub+=1
            l+=1
            r-=1
        print(rsub,lsub)
        return (rsub+lsub-1) if (rsub+lsub)>=3 else 0
