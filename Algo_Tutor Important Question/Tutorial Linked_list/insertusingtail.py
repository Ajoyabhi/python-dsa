class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
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

    def printll(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next



def main():
    ll = Linkedlist()
    value = list(map(int, input().split()))
    for i in range(len(value)):
        ll.insertusingtail(value[i])

    ll.printll()


if __name__ =='__main__':
    main()
