class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    

class Linkedlist:
    def __init__(self):
        self.head=None

    def appendnode(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
            current_node.next=new_node

    def printll(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.data,end=" ")
            current_node=current_node.next
        print("\n")


    def sortedMerge(self, a, b):
        result = None
         
        # Base cases
        if a == None:
            return b 
        if b == None:
            return a
             
        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
    def mergeSort(self,h):
        if h == None or h.next == None:
            return h
        else:
            middle=self.getMiddle(h)
            nexttomiddle=middle.next
            middle.next=None
            left=self.mergeSort(h)
            right=self.mergeSort(nexttomiddle)


            sortedlist=self.sortedMerge(left,right)
            return sortedlist



    #function for finding second last element.a
    def secondlast(self):
        current_node=self.head
        while current_node.next.next != None:
            current_node=current_node.next
        print(current_node.data)





     
    # Utility function to get the middle
    # of the linked list
    def getMiddle(self,head):
        if head is None:
            return head
        slow=head
        fast=head



        while fast.next != None and fast.next.next != None:
            slow=slow.next
            fast=fast.next.next

        return slow






li=Linkedlist()
li.appendnode(8)
li.appendnode(3)
li.appendnode(4)
li.appendnode(7)



print("Before Sorting.....!!!!")

li.printll()
li.head=li.mergeSort(li.head)




print("After  Sorting.....!!!!")

li.printll()


li.secondlast()

        

