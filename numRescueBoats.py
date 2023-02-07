class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l,r=0,len(people)-1
        cnt=0
        people.sort()
        while l<=r:

            sm=people[l]+people[r]
            if sm<=limit:
                l+=1
                r-=1
            else:
                if people[r]>=people[l]:
                    r-=1
                else:
                    l+=1
            cnt+=1
        return cnt     
