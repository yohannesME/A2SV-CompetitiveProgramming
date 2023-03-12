# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = None

        def findMiddle(head):
            tortoise = head
            prevTotortoise = head
            rabbit = head
        
            while rabbit and rabbit.next:
                prevTotortoise = tortoise
                tortoise = tortoise.next
                rabbit = rabbit.next.next
            
            prevTotortoise.next = None
            return tortoise
        
        def sortedListMerge(list1, list2):
            dummy = cur = ListNode(0)
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 or list2
            return dummy.next

        def sortlinkedlist(head):
            if not head:
                return
            
            if not head.next:
                return head
            
            middle = findMiddle(head)

            if not middle:
                return

            secondHalf = sortlinkedlist(middle)
            firstHalf = sortlinkedlist(head)

            return sortedListMerge(firstHalf, secondHalf)


        return sortlinkedlist(head)