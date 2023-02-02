# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #the answer stored on another listnodes
        answer = ListNode()
        #record if the sum at each point is greater of equal to 10
        remaining = 0
        #if at last their is no remainder just delete the next val so keep track
        lastBeforeRemain = None
        head = answer
        #if one is greater than the other
        while l1 or l2:
            #there is something to add
            if l1 and l2:
                val = l1.val + l2.val + remaining
                remaining = 0
                if val > 9:
                    answer.val =(val%10)
                    remaining = val//10
                else:
                    answer.val = val
                #move the pointer of the l1 and l2
                l1 = l1.next
                l2 = l2.next
            #when their is nothing to add just append but check the remainder
            elif l1:
                val = l1.val + remaining
                remaining = 0
                if val > 9:
                    answer.val =(val%10)
                    remaining = val//10

                else:
                    answer.val = val
                #move the pointer of the l1
                l1 = l1.next
            elif l2:
                val = l2.val + remaining
                remaining = 0
                if val > 9:
                    answer.val =(val%10)
                    remaining = val//10
                else:
                    answer.val = val
                #move the pointer of the l2
                l2 = l2.next
            #moveto the next answer
            answer.next = ListNode()
            #hold last before
            lastBeforeRemain = answer
            answer = answer.next
            
            
        #if we add their is no remainder just delete else update
        if remaining != 0:
            answer.val = remaining
        else:
            lastBeforeRemain.next = None
    
        #return the that keep tracks of the answer List Nodes
        return head