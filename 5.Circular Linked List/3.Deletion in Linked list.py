# CIRCULAR LINKED LIST (CREATE & DISPLAY)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        if self.head is None:
            print("Empty CLL") 
        else:
            temp = self.head
            print(temp.data, "->", end='')
            while temp.next is not self.head:
                temp = temp.next
                print(temp.data, "->", end='') 
            print(temp.next.data )

    def delete_start(self):
        if self.head is None:
            print("No Node to delete Empty CLL")
        else:
            if self.head==self.tail:
                self.head=None
            else:
              temp=self.head
              self.head=temp.next
              self.tail.next=self.head
              temp=None

    def delete_end(self):
        if self.head is None:
            print("No Node to delete Empty CLL")
        else:
            if self.head==self.tail:
                self.head=None
            else:
                temp=self.head
                while temp.next is not self.tail:
                        temp=temp.next
                self.tail=None
                self.tail=temp
                self.tail.next=self.head

    def delete_position(self,pos):
        if self.head is None:
            print("No Node to delete Empty CLL")
        elif pos == 1:
            self.delete_start()
        
        else:
            temp= self.head.next
            prev=self.head
            for i in range (1,pos-1):
                temp=temp.next
                prev=prev.next
            prev.next= temp.next
            temp=None
            if temp == self.tail:
                self.tail=prev
                self.tail.next=self.head
                temp=None
            

l=CLL()

n1=Node(10)
l.head=n1
l.tail=n1
l.tail.next=l.head

n2=Node(20)
l.tail.next=n2
l.tail=n2
l.tail.next=l.head

n3=Node(30)
l.tail.next=n3
l.tail=n3
l.tail.next=l.head

n4=Node(40)
l.tail.next=n4
l.tail=n4
l.tail.next=l.head

n5=Node(50)
l.tail.next=n5
l.tail=n5
l.tail.next=l.head

n6=Node(60)
l.tail.next=n6
l.tail=n6
l.tail.next=l.head

n7=Node(70)
l.tail.next=n7
l.tail=n7
l.tail.next=l.head
l.display()

l.delete_start()
l.display()
l.delete_end()
l.display()
l.delete_position(3)
l.display()