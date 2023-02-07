class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p2=0

        for p1 in range(len(nums)):

            if nums[p1]:
                nums[p1],nums[p2]=nums[p2],nums[p1]
                p2+=1
      

            

