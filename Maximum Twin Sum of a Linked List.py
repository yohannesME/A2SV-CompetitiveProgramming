# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        sum = 0
        temp = head
        stack = []
        while temp:
            stack.append(temp.val)
            temp = temp.next
        while head:
            sum = max(sum, head.val + stack.pop())
            head = head.next
        return sum
