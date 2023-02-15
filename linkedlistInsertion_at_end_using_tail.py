class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertionAtEnd(self,data):
        newnode = Node(data)
        if(self.head is None):
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def printlinkedlist(self):
        temp = self.head
        while(temp is not None):
            print(temp.data,end='')
            print(temp,end='')
            print(temp.next)
            temp = temp.next

def main():
    singlyatend = linkedList()
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        singlyatend.insertionAtEnd(arr[i])
    singlyatend.printlinkedlist()

if __name__=='__main__':
    main()