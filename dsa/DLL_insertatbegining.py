class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class linklist:
    def __init__(self):
        self.head = None


    def insertatbegining(self, data):
        newnode = node(data)
        if (self.head is None):
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    def printDL(self):
        temp = self.head
        while (temp is not None):
            print(temp.data, end=' ')
            temp = temp.next


def main():
    doublyLinklist = linklist()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        doublyLinklist.insertatbegining(arr[i])
    doublyLinklist.printDL()


if __name__ == '__main__':
    main()