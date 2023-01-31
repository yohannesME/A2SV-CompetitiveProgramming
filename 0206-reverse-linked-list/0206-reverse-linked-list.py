# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #hold the reversed linked list location
        prev = None
        current = head
        
        #where there is a value
        while current:
            temp = current.next
            #reverse it and move on to the next
            current.next = prev
            prev = current
            
            current = temp
            
        return prev