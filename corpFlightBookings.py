class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*n

        for book in bookings:
            first,last,seats=book
            ans[first-1]+=seats
            if last<n:
                ans[last]-=seats
       
        for i in range(1,n):

            ans[i]=ans[i-1]+ans[i]
        return ans
