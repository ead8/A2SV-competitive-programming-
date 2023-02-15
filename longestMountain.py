class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        incre,decre,ans = 0,0,0
        for i in range(1, len(arr)):
            if (decre and arr[i-1] < arr[i]) or arr[i-1] == arr[i]:
                incre,decre = 0, 0
            incre += arr[i-1] < arr[i]
            decre += arr[i-1] > arr[i]

            if incre  and decre:
                ans = max(ans, incre + decre + 1)
        return ans 
