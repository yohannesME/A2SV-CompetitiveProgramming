# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #get the size of the nodes
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
            
        #if size == n are 1 then return none
        if size-n-1 == -1:
            return head.next
        
        
        #as n is always lower than node length just traverse
        current = head
        for _ in range(size-n-1):
            current = current.next
        
        #update current next to next next
        current.next = current.next.next
        
        return head
        