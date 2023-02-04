# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        #floyd algorithm
        rabbit = head
        tortoise = head
        
        #if one node travels one at a time and another twice as fast they are bound to meet sometimes
        while tortoise.next and tortoise.next.next:
            rabbit = rabbit.next
            tortoise = tortoise.next.next
            if rabbit == tortoise:
                tortoise = head
                while rabbit != tortoise:
                    rabbit = rabbit.next
                    tortoise = tortoise.next
                    
                return rabbit
        return None