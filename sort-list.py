# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #finds the middle of the current linked list
    def findMiddle(self,head):
        #this variable is used to cut of the head pointer right before the middle one
        prevTotortoise = head
        #straight forward tortoise and rabbit algorithm to find the middle
        tortoise = head
        rabbit = head
    
        while rabbit and rabbit.next:
            prevTotortoise = tortoise
            tortoise = tortoise.next
            rabbit = rabbit.next.next
        
        prevTotortoise.next = None
        return tortoise

    #merge two sorted list
    def sortedListMerge(self,list1, list2):
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

    #cut the list into half each time until there is only one element and build it up again but this time sorted.
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        if not head.next:
            return head
        
        middle = self.findMiddle(head)

        if not middle:
            return

        secondHalf = self.sortList(middle)
        firstHalf = self.sortList(head)

        return self.sortedListMerge(firstHalf, secondHalf)