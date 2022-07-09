# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # temp = head
        # while temp.next != None:
        #     prev = temp
        #     if temp.next == None:
        #         return head
        #     temp = temp.next
        #     if prev.val == temp.val:
        #         if temp.next == None:
        #             prev.next = None
        #             return head
        #         prev.next = temp.next
        #         temp = temp.next
        # return head
        temp = head
        store = []
        while temp != None:
            store.append(temp.val)
            temp = temp.next
        store = list(store)
        store = sorted(set(store), key=store.index)
        if len(store) == 0:
            return None
        head = ListNode(store[0])
        temp = head
        for i in range(1, len(store)):
            temp.next = ListNode(store[i])
            temp = temp.next
        return head
