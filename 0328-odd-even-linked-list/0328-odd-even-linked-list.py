# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if two or less element return it back
        if not (head and head.next):
            return head
        
        #the first element is even get it and move forward
        even = head
        head = head.next
        even.next = None
        #the second element is odd get amd move forward
        odd = head
        head = head.next
        odd.next = None
        
        #start from even and odd and add to them while we traverse head
        back = even
        front = odd

        while head:
            back.next = head
            head = head.next
            back = back.next
            back.next = None
            if head:
                front.next = head
                front = front.next
                head = head.next
                front.next = None
            else:
                break

        #when we finish then we add at the end of the even the odd values
        back.next = odd
        return even

            