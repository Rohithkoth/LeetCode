# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        curr = head
        prev = ListNode(0) 
        prev.next = curr
        while l1 and l2:
            print(curr.val)
            
            if( curr.val + l1.val + l2.val )>=10:
                curr.next = ListNode(1)
            else:
                curr.next = ListNode(0)
            curr.val=(curr.val + l1.val+l2.val)%10
            prev = curr
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
            print(curr.val)

        while l2:
            
            if curr.val + l2.val >=10:
                curr.next = ListNode(1)
            else:
                curr.next = ListNode(0)
            curr.val=(curr.val+l2.val)%10
            prev = curr
            l2 = l2.next
            curr = curr.next

        while l1:
            
            if curr.val + l1.val >=10:
                curr.next = ListNode(1)
            else:
                curr.next = ListNode(0)
            curr.val=(curr.val+l1.val)%10
            prev = curr
            l1 = l1.next
            curr = curr.next
        if curr.val == 0:
            prev.next = None

        return head