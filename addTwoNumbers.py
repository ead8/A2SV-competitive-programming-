# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# import itertools
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=''
        s2=''
        while l1 or l2:
            if l1:
                s1+=str(l1.val)
                l1=l1.next
            elif l1 is None:
                s1+='0'
            if l2:
                s2+=str(l2.val)
                l2=l2.next
            elif l2 is None:
                s2+='0'
        sum=str(int(s1[::-1])+int(s2[::-1]))
       
        nodeList=list(sum)
        for i,n in enumerate(sum):
            if i==0:
                nodeList[i]=ListNode(val=n,next=None)
            else:
                nodeList[i]=ListNode(val=n,next=nodeList[i-1])
        return nodeList[len(sum)-1]


    


