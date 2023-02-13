# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # edge case
        if head.next.next == None :
            return head.val + head.next.val
        dict = {} # key = i, value = pair sum
        slow, fast = head, head 
        i = 0 #slow index
        while fast and fast.next :
            dict[i] = slow.val
            slow = slow.next
            fast = fast.next.next
            i += 1
        n = i*2 #total length of the link list
        maxVal = 0
        while slow :
            maxVal = max(maxVal, dict[n - i - 1] + slow.val)
            slow = slow.next
            i += 1
        return maxVal

