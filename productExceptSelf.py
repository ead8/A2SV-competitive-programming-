class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans=[1]*len(nums)
        pref=postf=1

        for i in range(len(nums)):
            ans[i]=pref
            pref*=nums[i]
        ans=ans[::-1]
        for i,n in enumerate(nums[::-1]):
            ans[i]*=postf
            postf*=n
        return ans[::-1]


