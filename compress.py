class Solution:
    def compress(self, chars: List[str]) -> int:
        s=''
        l=r=0
        cnt=0
        while r<len(chars):
            
            if chars[l]==chars[r]:
                r+=1
                cnt+=1
            elif chars[l]!=chars[r]:
                s+=chars[l]
                l=r
                if cnt>1:
                    s+=str(cnt)
                cnt=0
        s+=chars[l]
        if cnt>1:
            s+=str(cnt)
        chars[:]=[c for c in s]
        return len(chars)
           
