class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
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
l.display()
