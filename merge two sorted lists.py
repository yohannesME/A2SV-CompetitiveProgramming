# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = list1
        store = []
        while temp != None:
            store.append(temp.val)
            temp = temp.next
        temp = list2
        while temp != None:
            store.append(temp.val)
            temp = temp.next
        store.sort()
        if len(store) == 0:
            return None
        head = ListNode(store[0])
        temp = head
        for i in range(1, len(store)):
            temp.next = ListNode(store[i])
            temp = temp.next
        return head        
        
