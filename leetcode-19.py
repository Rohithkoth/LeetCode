# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        canary = head
        length=0
        while canary != None:
            length +=1 
            canary = canary.next
        

        curr =head
        prev = ListNode(0,head)
        out = prev
        for i in range(length-n):
            curr = curr.next
            prev = prev.next
        
        prev.next=curr.next

        return out.next


            