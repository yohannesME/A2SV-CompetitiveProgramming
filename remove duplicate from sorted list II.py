# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        front = head
        back = dummy
        while front:
            if front.next and front.val == front.next.val:
                
                value = front.val
                while front and front.val == value:
                    front = front.next
                back.next = front
            else:
                front = front.next
                back = back.next
                    
        return dummy.next
