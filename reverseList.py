# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  #empty or 1 list
            print(head)
            return head
       
        new_head=self.reverseList(head.next)
        #make last node head head
        print(head)
        
        head.next.next=head

        head.next=None
        # print(head)
        return new_head











