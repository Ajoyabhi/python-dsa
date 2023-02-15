class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class linklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatend(self, data):
        newnode = node(data)
        if (self.head is None):
            self.head = newnode
            self.tail = newnode
            return
        else:
            self.tail.next = newnode

            newnode.prev = self.tail
            self.tail = newnode
    def deletionatend(self):
        if(self.head is None):
            return
        elif(self.head.next is None):
            self.head = None
        else:
            temp = self.tail.prev
            temp.next = None
            self.tail.pre= None
            tail = temp
    def printDL(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=' ')
            temp = temp.next


def main():
    doublyLinklist = linklist()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        doublyLinklist.insertatend(arr[i])
    doublyLinklist.deletionatend()
    doublyLinklist.printDL()


if __name__ == '__main__':
    main()