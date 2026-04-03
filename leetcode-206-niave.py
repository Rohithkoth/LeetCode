# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if head == None:
            return head
        while head != None:
            nex = head.next
            head.next = prev
            prev = head
            if nex == None:
                return head
            head = nex
        # return head