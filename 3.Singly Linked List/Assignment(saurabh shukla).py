#singly linked list
# q1)Define a class Node to describe a node of a singly linked list.
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next 
#q2)Define a class SLL to implement Singly Linked List with __init__() method to create and initialise start reference variable.
class SLL:
    def __init__(self,start=None):
        self.start=start
#q3)Define a method is_empty() to check if the linked list is empty in SLL class.
    def is_empty(self):
        return self.start==None 
#q4)In class SLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self,data):
        n=Node(data,self.start)     
        self.start=n
#q5)In class SLL, define a method insert_at_last() to insert an element at the end of the list.
    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next  #ek ek node pudhe janar
            temp.next=n
        else:
            self.start=n
#q6)In class SLL, define a method search() to find the node with specified element value.
    def search(self,data):
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    return temp
                temp=temp.next  #ek ek node pudhe janar
            return None
#q7)In class SLL, define a method insert_after() to insert a new node after a given node of the list.
    def insert_after(self,temp,data):
            if temp is not None:
               n=Node(data,temp.next)
               temp.next=n
#q8)In class SLL, define a method to print all the elements of the list.
    def print_list(self):
            temp=self.start
            while temp is not None:
               print(temp.item,end=' ')
               temp=temp.next
#q10)In class SLL, define a method delete_first() to delete first element from the list
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
#q11)In class SLL, define a method delete_last() to delete last element from the list.
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
#q12)In class SLL, define a method delete_item() to delete specified element from the list.
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
#q9)In class SLL, implement iterator for SLL to access all the elements of the list in a sequence.
    def __iter__(self):
        return SLLIterator(self.start)
class SLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
                 

#driver code
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(30)
print()

for x in mylist:
    print(x,end=' ')

print()
