class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        r=l=0
        ans=0
        hashmap={}
        while r<len(s):
            if s[r] not in hashmap:
                hashmap[s[r]]=r
                r+=1
                ans=max(ans,r-l)
            else:
                hashmap.pop(s[l])
                l+=1
        return ans

