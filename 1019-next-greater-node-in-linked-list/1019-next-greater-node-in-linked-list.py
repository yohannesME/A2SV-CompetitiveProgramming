# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        #reverse the linked list
        current = head
        prev = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        #the result
        result = []
        #stack to keep track of the largest value
        stack = []

        #traverse through the reversed nodes
        current = prev
        while current:
            #find the max value in the accumulated stack
            while len(stack) > 0 and stack[-1] <= current.val:
                stack.pop()
                
            #if there is no value to the stack add zero as the element is the largest if value in the stack add that value as it is the largest
            if len(stack) == 0:
                result.append(0)
            else:
                result.append(stack[-1])
            
            #add to the stack current value and move forward
            stack.append(current.val)
            current = current.next
            
        #reverse the answr and add them
        result.reverse()
        return result
        