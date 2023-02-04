# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        #floyd algorithm
        rabbit = head
        tortoise = head
        
        #if one node travels one at a time and another twice as fast they are bound to meet sometimes
        while tortoise.next and tortoise.next.next:
            rabbit = rabbit.next
            tortoise = tortoise.next.next
            if rabbit == tortoise:
                return True
        return False