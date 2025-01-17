class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertusingtail(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        self.tail.next = newnode
        self.tail = newnode

    def insertAtnthNode(self, data, position):
        newnode = Node(data)
        if position == 0:
            newnode.next = self.head
            self.head = newnode
        count = 0
        temp = self.head

        while temp is not None and (count < position - 1):
            temp = temp.next
            count +=1

        if temp is None:
            print("invalid position is given!! inserting at end")
            self.insertatend(data)

        newnode.next = temp.next
        temp.next = newnode


    def insertatend(self,data):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next

        newnode = Node(data)
        temp.next = newnode

    def printll(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=' ')
            temp = temp.next

def main():
    ll = linkedlist()
    value = list(map(int, input().split()))
    for i in range(len(value)):
        ll.insertusingtail(value[i])
    ll.printll()
    print()
    ll.insertAtnthNode(100,3)
    ll.printll()

if __name__ == '__main__':
    main()
