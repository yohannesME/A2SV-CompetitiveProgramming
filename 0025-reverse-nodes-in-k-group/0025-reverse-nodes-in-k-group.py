# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #the answer head is put here
        answer = None
        
        #if k is 1 just return the same head
        if k == 1:
            return head
        
        #find the length of t he linked list
        size = 0
        current = head
        while current:
            current = current.next
            size += 1
        
        #find the group to iterate
        group = size//k
        
        #loop through the group and reverse
        prev = None
        current = head
        for i in range(group):
            #reverse the groups
            for j in range(k):
                if j == 0:
                    joiningPoint = current
                
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            #prev is the begining and joining point is the end
            if i == 0:
                answer = prev
                tempJoin = joiningPoint
                tempJoin.next = None
            else:
                tempJoin.next = prev
                tempJoin = joiningPoint
                tempJoin.next = None
                
        if current:
            tempJoin.next = current
        
        
        return answer