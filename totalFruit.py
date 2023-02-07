class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l=max_len=0
        v={}
        for r in range(len(fruits)):
            
            v[fruits[r]]=r
    
            if len(v)==3:
                min_indx=min(v.values())
                
                v.pop(fruits[min_indx])
                l=min_indx+1
            max_len=max(max_len,r-l+1)
        
        return max_len
                



            

