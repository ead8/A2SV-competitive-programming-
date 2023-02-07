class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #2^31-1, the biggest power of three value is determined. 
        return n > 0 and 3**19 % n == 0
