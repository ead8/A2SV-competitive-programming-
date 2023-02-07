
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        # 1. compute prefix sum 
       
        for i in range(len(A)):
            if i > 0:
                A[i]+=A[i-1]
        A.insert(0,0)   # to make easy for competion

        # 2 then callculate L length Subarray sum Before M
        # we take sum of L number of items first then we take the rest sum of M items
        # |----L--- |---M---]
        # loop by L+M since it's the total length of Current window
        print(A)
        res = 0
        Lmax = 0
        Mmax = 0
        for l in range(L+M,len(A)):

            # Take L first
            Lsum = A[l-M] - A[l-M-L]
            Msum = A[l] - A[l-M]
            
            Lmax = max(Lmax,Lsum)
            res = max(res,Lmax+Msum)
          
            # Take M first
            Lsum = A[l] - A[l-L]
            Msum =  A[l-L] - A[l-L-M]
            
            Mmax = max(Mmax,Msum)
            res = max(res,Mmax+Lsum)

        # 3 then callculate M length Subarray sum Before L
        # we take sum of M number of items first then we take the rest sum of L items
        # |----M--- |---L---]

        # for m  in range(L+M, len(A)):
        #     Lsum = A[m] - A[m-L]
        #     Msum =  A[m-L] - A[m-L-M]
            
        #     Mmax = max(Mmax,Msum)
        #     res = max(res,Mmax+Lsum)
        
        return res


                

