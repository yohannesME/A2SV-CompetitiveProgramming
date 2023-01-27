class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.head = None
        
    def printAll(self)-> None:
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next
        print('done')
        
    def get(self, index: int) -> int:
        temp = self.head
        for i in range(index):    
            temp = temp.next
            if temp == None:
                return -1
        if temp == None:
            return -1
        return temp.val 
        

    def addAtHead(self, val: int) -> None:
        #if no recorded element just add the new val as a head else move the head to the next element and make the new node the head
        if not self.head:
            self.head = Node(val)
        else:
            newNode = Node(val)
            temp = self.head
            self.head = newNode
            self.head.next = temp
            newNode = None
        

    def addAtTail(self, val: int) -> None:
        #fist reach the end of the node and then the last node next will be the new node
        if self.head == None:
            self.head = Node(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)
            
            
    def addAtIndex(self, index: int, val: int) -> None:
        #if index 0 just add as a first element
        if index == 0:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
            return
        #if no head then
        if self.head == None:
            return
        temp = self.head
        for i in range(index-1):
            if  temp == None:
                return
            temp = temp.next
        if temp == None:
            return
        before = temp.next
        temp.next = Node(val)
        temp.next.next = before
                
                

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return
        temp = self.head
        for i in range(index-1):
            if temp == None:
                return
            temp = temp.next
        if temp == None:
            return
        toDelete = temp.next
        if toDelete:
            temp.next = temp.next.next
        toDelete = None

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)