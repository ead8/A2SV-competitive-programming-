class Solution:
    def hIndex(self, citations: List[int]) -> int:

        return sum([i<cit for i,cit in enumerate(sorted(citations,reverse=True))])







            
            
            
