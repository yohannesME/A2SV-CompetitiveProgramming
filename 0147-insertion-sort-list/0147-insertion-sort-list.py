# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head or head.next):
            return head
        
        answer = head
        
        head = head.next
        answer.next = None
        
        while head:
            inserted = False
            #if the first element
            #when inserting on the first element
            if head.val < answer.val:
                temp = head.next
                head.next = answer
                answer = head
                head = temp
                inserted = True
            #in the middle insertion
            else:
                current = answer
                while current.next:
                    if current.next.val < head.val:
                        current = current.next
                    else:
                        temp = current.next
                        headTemp = head.next
                        
                        current.next = head
                        current.next.next = temp
                        head = headTemp
                        inserted = True
                        break
                if current and head:
                    
                    if not inserted:
                        temp = head.next
                        head.next = None
                        current.next = head
                        head = temp
                        
            # print(head,answer,sep='\n')
        return answer
        