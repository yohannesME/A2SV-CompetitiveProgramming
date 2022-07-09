# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        while l1 != None:
            num1.append(l1.val)
            l1 = l1.next
        num2 = []
        while l2 != None:
            num2.append(l2.val)
            l2 = l2.next
        num1.reverse()
        num2.reverse()
        n1 = ''
        n2 = ''
        for i in num1:
            n1 += str(i)
        for i in num2:
            n2 += str(i)

        result = eval(n1+"+"+n2)
        result = str(result)
        result = [int(r) for r in result]
        result.reverse()
        answer = ListNode(result[0])
        temp = answer
        for i in range(1,len(result)):
            temp.next = ListNode(result[i])
            temp = temp.next

        return answer
