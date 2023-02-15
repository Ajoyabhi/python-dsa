class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertatend(self, data):
        newnode = node(data)
        if (self.head is None):
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def lastelementfirst(self):
        sec_last = None
        temp = self.head
        if (temp is None or temp.next is None):
            return
        while(temp.next is not None):
            sec_last = temp
            temp = temp.next

        sec_last.next = None
        temp.next = self.head
        self.head = temp
        return self.head

    def printlinkedlist(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end=' ')
            temp = temp.next
        print()

def main():
    ll = linkedlist()
    arr = list(map(int,input().split()))

    for i in range(len(arr)):
    #     print(arr[i])
        ll.insertatend(arr[i])
    ll.printlinkedlist()
    ll.lastelementfirst()
    ll.printlinkedlist()

if __name__ == '__main__':
    main()



