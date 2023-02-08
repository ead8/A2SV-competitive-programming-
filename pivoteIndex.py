class Solution:
 
    def pivotIndex(self, nums: List[int]) -> int:
        #prefix sum
        rightSum = sum(nums[1:])
        leftSum = 0
        #pivot index
        for i in range(len(nums)-1):
            if leftSum == rightSum:
                return i
            #prefix sum
            leftSum += nums[i]
            rightSum -= nums[i+1] #index out of range
        if rightSum == leftSum:
            return len(nums)-1
        return -1


