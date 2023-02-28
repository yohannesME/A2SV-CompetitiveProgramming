# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = ListNode()
        dummy.next = prev
        
        def merge( list1, list2):
            nonlocal prev
            if not list1 and not list2:
                return None
            if not list2 :
                prev.next = list1
                list1 = list1.next
                prev = prev.next
                prev.next = merge(list1,list2)
            elif not list1:
                prev.next = list2
                list2 = list2.next
                prev = prev.next
                prev.next = merge(list1,list2)
            else:
                if list1.val <= list2.val:
                    prev.next = list1
                    list1 = list1.next
                    prev = prev.next
                    prev.next = merge(list1,list2)
                elif list1.val > list2.val:
                    prev.next = list2
                    list2 = list2.next
                    prev = prev.next
                    prev.next = merge(list1,list2)

        merge(list1, list2)
        return dummy.next.next