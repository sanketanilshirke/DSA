class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None

    def insert_begining(self,data):
        nb= Node(data)
        nb.next=self.head
        self.head=nb
    
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne 

    def insert_position(self,pos,data):
         np=Node(data)
         temp=self.head
         for i in range(pos-1):
            temp=temp.next
         np.data=data
         np.next=temp.next
         temp.next=np

    def display(self):
        temp=self.head
        if self.head is None:
            print("Linked list is empty")
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next 

l=SLL()
n1=Node(10)
l.head=n1

n2=Node(20)
n1.next=n2

n3=Node(30) 
n2.next=n3

n4=Node(40)
n3.next=n4

n5=Node(50)
n4.next=n5

l.insert_begining(5)
l.insert_begining(2)

l.insert_end(60)
l.insert_end(70)

l.insert_position(4,25)

l.display()
