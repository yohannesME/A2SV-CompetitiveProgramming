# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        #if there is a value greater than one
        prev = head
        next = head.next
        while next:
            if prev.val == next.val:
                prev.next = next.next
                next = next.next
            else:
                prev = prev.next
                next = next.next
        return head

