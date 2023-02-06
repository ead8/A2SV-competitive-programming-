from collections import defaultdict
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d,count=defaultdict(int),0
    
        for num in nums:
            if d[num]:
                count+=1
                d[num]-=1
            else:
                d[k-num]+=1
        return count
