class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p=0
        i=-k
        while i<0:
            nums[i],nums[p]=nums[p],nums[i]
            p+=1
            i+=1
        if len(nums)%2!=0:
            nums.append(nums[-k-1])
            del nums[-k-2]

        print(nums)
