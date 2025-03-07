#Doubly Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL():
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head is None:
            print("DLL is Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<=>",end="")
                temp=temp.next
        
    def delete_beginning(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None

    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next.prev=prev
        temp.prev=None
        temp.next=None

l=DLL()
n1=Node(10)
l.head=n1

n2=Node(20)
n1.next=n2
n2.prev=n1

n3=Node(30)
n2.next=n3
n3.prev=n2

n4=Node(40)
n3.next=n4
n4.prev=n3

n5=Node(50)
n4.next=n5
n5.prev=n4

l.delete_beginning()
l.delete_end()
l.delete_position(2)
l.display()
