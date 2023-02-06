class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        nums=sorted(nums,key=lambda a:int(a),reverse=True)
        return str(nums[k-1])


