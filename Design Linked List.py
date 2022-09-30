class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        

class MyLinkedList:

    def __init__(self):
        self.myNode = None
        
    def printAll(self)-> None:
        temp = self.myNode
        while temp:
            print(temp.val)
            temp = temp.next
        print('done')
        
    def get(self, index: int) -> int:
        temp = self.myNode
        for i in range(index):    
            temp = temp.next
            if temp == None:
                return -1
        if temp == None:
            return -1
        return temp.val 
        

    def addAtHead(self, val: int) -> None:
        newNode = node(val)
        temp = self.myNode
        self.myNode = newNode
        self.myNode.next = temp
        newNode = None
        

    def addAtTail(self, val: int) -> None:
        if self.myNode == None:
            self.myNode = node(val)
            return
        temp = self.myNode
        while temp.next:
            temp = temp.next
        temp.next = node(val)
            
            

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            newNode = node(val)
            newNode.next = self.myNode
            self.myNode = newNode
            return
        if self.myNode == None:
            return
        temp = self.myNode
        for i in range(index-1):
            if  temp == None:
                return
            temp = temp.next
        if temp == None:
            return
        before = temp.next
        temp.next = node(val)
        temp.next.next = before
                
                

    def deleteAtIndex(self, index: int) -> None:

        if index == 0:
            if self.myNode:
                self.myNode = self.myNode.next
                return
        temp = self.myNode
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
