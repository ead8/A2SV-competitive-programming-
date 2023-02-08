class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum=0
        prefixSums={0:1}
        result=0
        for num in nums:
            curSum+=num
            diffr=curSum-k

            result+=prefixSums.get(diffr,0)
            prefixSums[curSum]=prefixSums.get(curSum,0)+1
            
        return result
