# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        if not head:
            return head
        
        
        reverse = ListNode(head.val)
        dummy = reverse
        current = head
        while current.next:
            reverse.next = ListNode(current.next.val)
            reverse = reverse.next
            current = current.next
        
        prev = None
        current = dummy
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        while head:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True
