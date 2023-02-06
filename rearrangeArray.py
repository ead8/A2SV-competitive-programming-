class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        smaller = True
        for i in range(1, len(nums)):
            if smaller and nums[i - 1] > nums[i] or not smaller and nums[i - 1] < nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            smaller = not smaller
        return nums
            
