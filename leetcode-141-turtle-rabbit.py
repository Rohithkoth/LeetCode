#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head 
        hare = head

        while hare != None and hare.next != None:
            if hare.next == turtle:
                return True
            hare = hare.next.next
            turtle = turtle.next
            

        return False