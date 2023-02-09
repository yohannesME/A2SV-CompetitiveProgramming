# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = head.val
        
        #binary of base 2 can be converted accordingly by multiplying it by two
        while head.next:
            answer = answer*2 + head.next.val
            head = head.next
        
        return answer