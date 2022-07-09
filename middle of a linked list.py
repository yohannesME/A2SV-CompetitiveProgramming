# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp != None:
            temp = temp.next
            count +=1
        
        count = count/2
        count = int(count)
        for i in range(count):
            head = head.next
            
        return head
        
