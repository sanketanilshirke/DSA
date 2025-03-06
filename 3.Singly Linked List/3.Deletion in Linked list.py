class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next

    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None

    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None


L=SLL()
n1=node(10)
L.head=n1
n2=node(20)
n1.next=n2
n3=node(30)
n2.next=n3
n4=node(40)
n3.next=n4
n5=node(50)
n4.next=n5
L.delete_begining()  #10
L.delete_end()    #50
L.delete_position(2)  # 20 --> 30 --> 40  , 30 del zale because (pos-1), 2-1= 1st position
L.display()



