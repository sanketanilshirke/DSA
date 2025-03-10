#1.Define a class Node to describe a node of a circular linked list.
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
# 2.Define a class CLL to implement Circular Linked List with __init__() method to create
# and initialise last reference variable.
class CLL:
    def __init__(self,last=None):
        self.last=last
#3.Define a method is_empty() to check if the linked list is empty in CLL class
    def is_empty(self):
        return self.last==None
#4.In class CLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
#5.In class CLL, define a method to insert an element at the end of the list
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
#6.In class CLL, define a method search() to find the node with specified element value.
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
#7.In class CLL, define a method to insert a new node after a given node of tne list.
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
#8.In class CLL, define a method to print all the elements of the list
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)
# 10.In class CLL, define a method delete_first() to delete first element from the list.
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
#11.In class CLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
#12.In class CLL, define a method delete_item() to del ete specified element from the list
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp=self.last.next

                    while temp!=self.last:
                        if temp.next==self.last:
                            if self.last.item==data:
                                self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                        temp=temp.next
#9.In class CLL, implement iterator for CLL to access all the elements of the list in a sequence. 
    def __iter__(self):
        if self.last==None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
            
class CLLIterator:
    def __init__(self,start):
        self.current=start 
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        
        return data

cll=CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
# 20 10 50 30 40
for x in cll:
    print(x,end=' ')
print()
cll.print_list()


    