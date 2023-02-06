class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums=sorted(nums)
        currentNo=None
        smallerNo=0
        counter={}
        for num in sortedNums:
            if num!=currentNo:
                counter[num]=smallerNo
                currentNo=num
            smallerNo+=1
        return [counter[x] for x in nums]
                        
