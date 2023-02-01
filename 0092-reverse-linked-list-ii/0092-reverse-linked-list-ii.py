# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #if they are equal no need to reverse
        if left == right:
            return head
        
        #first go forward until left is reached
        reverse = head
        lastFromStart = reverse
        for _ in range(left-1):
            #hold the last element before left to connect the reversed
            lastFromStart = reverse
            reverse = reverse.next
            
        prev = None
        lastFrom = reverse
        
        #the count of value to reverse
        toBeReversed = right-left+1     

        #where there is a value
        while toBeReversed > 0:
            temp = reverse.next
            #reverse it and move on to the next
            reverse.next = prev
            prev = reverse
            
            reverse = temp
            toBeReversed -= 1
            
        #if left starts from head no need to check what comes before
        if left != 1:
            lastFrom.next = reverse
            lastFromStart.next = prev
        else:
            lastFrom.next = reverse
            return prev
        
        return head