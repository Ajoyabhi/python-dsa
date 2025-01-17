class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertatbegg(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printll(self):
        temp = self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next


def main():
    ll = Linkedlist()
    value = list(map(int, input().split()))
    for i in range(len(value)):
        ll.insertatbegg(value[i])

    ll.printll()


if __name__ =='__main__':
    main()
