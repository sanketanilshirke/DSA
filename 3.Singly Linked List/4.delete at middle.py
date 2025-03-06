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

    def middle_delete(self):
            if self.head is None:
                print("empty linked list")
            else:
                if self.head.next is None:
                    print("one node contain no middle to delete")
                else:
                    temp=self.head
                    slow=self.head
                    fast=self.head
                    while fast is not None and fast.next is not None:
                        fast= fast.next.next
                        slow=slow.next
                    while temp.next is not slow:
                        temp=temp.next
                    temp.next = slow.next
                    slow=None



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


l.middle_delete()
l.display()
