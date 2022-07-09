# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        store = []
        while temp != None:
            store.append(temp.val)
            temp = temp.next
        
        stack = []
        result = []
        store.reverse()
        for i in range(len(store)):
            while len(stack) > 0 and stack[-1] <= store[i]:
                stack.pop()
            if len(stack) == 0:
                result.append(0)
            else:
                result.append(stack[-1])
            stack.append(store[i])
            
        result.reverse()
        return result
        
