# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fastp=head
        slowp=head
        for i in range(n):
            fastp=fastp.next
        if not fastp:
            return head.next
        while fastp.next:
            slowp=slowp.next
            fastp=fastp.next
        slowp.next=slowp.next.next
        return head

