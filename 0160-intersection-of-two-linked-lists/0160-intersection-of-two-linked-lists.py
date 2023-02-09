# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = 0
        current = headA
        while current:
            current = current.next
            sizeA += 1
        
        sizeB = 0
        current = headB
        while current:
            current = current.next
            sizeB += 1
        
        if sizeA > sizeB:
            for _ in range(sizeA-sizeB):
                headA = headA.next
        elif sizeB > sizeA:
            for _ in range(sizeB-sizeA):
                headB = headB.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
        
        