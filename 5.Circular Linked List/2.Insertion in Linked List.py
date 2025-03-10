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


    def insert_begin(self,data):
        n1= Node(data)
        if self.head is None:
            self.head=n1
            self.tail=n1
            self.tail.next=self.head
        else:
            n1.next=self.head
            self.tail.next=n1
            self.head=n1

    def insert_end(self,data):
        n1= Node(data)
        if self.head is None:
            self.head=n1
            self.tail=n1
            self.tail.next=self.head
        else:
            n1.next=self.head
            self.tail.next=n1
            self.tail=n1

    def insert_position(self,pos,data):
        n1= Node(data)
        if self.head is None:
            self.head=n1
            self.tail=n1
            self.tail.next=self.head
        else:
            if pos==1:
                self.insert_begin(data)
            else:
             temp=self.head
             for i in range(1,pos-1):
                  temp=temp.next
             n1.next=temp.next
             temp.next=n1

l=CLL()

l.insert_begin(10)
l.display()
l.insert_begin(5)
l.display()

l.insert_end(20)
l.display()
l.insert_end(30)
l.display()

#insertion of 15 at position 3
l.insert_position(3,15)
l.display()
l.insert_position(5,25)
l.display()
l.insert_position(1,0)
l.display()


