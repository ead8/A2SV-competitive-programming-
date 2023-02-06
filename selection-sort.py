#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(1,len(arr)):
            crr=self.select(arr,i)
            for j in range(i):
                if crr<arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
                    


