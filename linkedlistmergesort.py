class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def appendLast(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node


    def printLL(self):
        if self.head is None:
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,end = " ") 
                temp=temp.next

            

    def sortedMerge(self,a,b):
        result = None
        if a == None:
            return b
        elif b == None:
            return a

        else:
             if a.data <= b.data:
                result = a
                result.next = self.sortedMerge(a.next,b)
             else:
                result = b
                result.next = self.sortedMerge(a,b.next)
        
        return result


    def getMiddle(self,head):
        if head is None:
            return head
        else:
            slow = head
            fast = head


            while fast.next != None and fast.next.next != None:
                slow = slow.next
                fast = fast.next.next


        return slow



    def mergeSort(self,h):
        if h == None or h.next == None:
            return h
        else:
            middle = self.getMiddle(h)
            nexttomiddle = middle.next
            middle.next = None

            left = self.mergeSort(h)
            right = self.mergeSort(nexttomiddle)


            mergesortedlist = self.sortedMerge(left,right)

            return mergesortedlist





li=LinkedList()

li.appendLast(5)


li.appendLast(8)


li.appendLast(3)


li.appendLast(6)



print("Before Sorting ...")

li.printLL()
print("\n")


li.head = li.mergeSort(li.head)

print("After Sorting...")
print("\n")


li.printLL()


print("\n")
             