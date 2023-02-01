# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        #to be updated when first encountered
        nodesGreater = None
        nodesLesser = None
        
        currentLess = nodesLesser
        currentGreater = nodesGreater
        
        current = head
        while current:
            if current.val < x:
                if not currentLess:
                    nodesLesser = ListNode(current.val)
                    currentLess = nodesLesser
                else:
                    currentLess.next = ListNode(current.val)
                    currentLess = currentLess.next
            else:
                if not currentGreater:
                    nodesGreater = ListNode(current.val)
                    currentGreater = nodesGreater
                else:
                    currentGreater.next = ListNode(current.val)
                    currentGreater = currentGreater.next
            current = current.next

        if not head:
            return None
        elif not nodesLesser:
            return nodesGreater
        else:
            currentLess.next = nodesGreater
            return nodesLesser