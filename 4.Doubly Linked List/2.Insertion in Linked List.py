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

    def insert_begining(self,data):
        n=Node(data)
        self.head.prev=n
        n.next=self.head
        self.head=n

    def insert_end(self,data):
        n=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp

    def insert_position(self,pos,data):
        n=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
       


l=DLL()
n1=Node(10)
l.head=n1

n2=Node(20)
n1.next=n2
n2.prev=n1

n3=Node(30)
n2.next=n3
n3.prev=n2

l.insert_begining(5)
l.insert_end(40)
l.insert_position(3,15)

l.display()
