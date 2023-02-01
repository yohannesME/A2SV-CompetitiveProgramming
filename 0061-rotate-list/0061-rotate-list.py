# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        prev = None
        
        size = 0
        while current:
            current = current.next
            size += 1
        
        #if there is no element
        if size == 0:
            return head
        
        #if k is larger than size
        if k >= size:
            k = k%size
        
        #no need to ratote it will be back to the original
        if k == 0:
            return head  
        
        current = head
        
        #reverse the nodes
        while current:
            temp = current.next
            current.next = prev
            prev = current
            
            current = temp
        

        
        #before reverse the first element is the point we append the second reverse
        lastFirst = prev
        current = prev
        prev = None
        
        firstR = k
        #reverse the k + elements
        for _ in range(firstR):
            temp = current.next
            current.next = prev
            prev = current
            
            current = temp
        
        #the reversed first part of the linked list is the start of the answer
        answer = prev
        prev = None
        
        for _ in range(size-k):
            temp = current.next
            current.next = prev
            prev = current
            
            current = temp
        
        lastFirst.next = prev
        
        return answer