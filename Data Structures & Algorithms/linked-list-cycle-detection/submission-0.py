# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Sptr = head
        Fptr = head

        while Fptr and Fptr.next:
            Sptr = Sptr.next
            Fptr = Fptr.next.next
            if Sptr == Fptr:
                return True
        return False