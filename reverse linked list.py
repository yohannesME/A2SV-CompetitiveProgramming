# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        store = []
        while temp != None:
            store.append(temp.val)
            temp = temp.next
        store.reverse()
        if len(store) == 0:
            return None
        head = ListNode(store[0])
        temp = head
        for i in range(1, len(store)):
            temp.next = ListNode(store[i])
            temp = temp.next
        return head
