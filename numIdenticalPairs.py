class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        cnt=0
        nums.sort()
        for i in range(len(nums)):

           for j in range(len(nums)):
               if nums[i]==nums[j] and i<j:
                   cnt+=1

        return cnt
