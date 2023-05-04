# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # let's input list of lined list to the heap
        heap = []
        ans = ListNode()
        head = ans

        for index, sortedList in enumerate(lists):
            if sortedList:
                heap.append((sortedList.val,index, sortedList))

        # Create a heap Structure
        heapify(heap)
        
        # While there is element in the heap
        while heap:
            #pop the value,  identification , and linked list that is minimum
            val , index , node = heappop(heap)
            # Concatenate to our answer
            head.next = node
            head = head.next
            node = node.next

            # Add the Adjacent Value to the heap if any
            if node:
                heappush(heap, (node.val , index ,  node))

        # Using the Dummy we set as Answer we Anwer
        return ans.next