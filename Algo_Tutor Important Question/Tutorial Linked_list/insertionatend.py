class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insertatbeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = newnode

    def printnode(self):
        temp = self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next



if __name__ =='__main__':
    ll  = linkedlist()
    ll.insertatbeg(2)
    ll.insertatbeg(12)
    ll.insertatbeg(32)
    ll.insertatbeg(52)
    ll.insertatbeg(62)
    ll.insertatbeg(72)
    ll.printnode()



