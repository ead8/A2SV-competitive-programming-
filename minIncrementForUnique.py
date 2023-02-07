class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        result=0
        nums.sort()
        for i in range(1,len(nums)):
            
            prev=nums[i-1]
            cur=nums[i]
            if prev>=cur:
                result+=prev-cur+1
                nums[i]=prev+1
        return result
