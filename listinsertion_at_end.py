class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    def insertAtEnd(self,data):
        newnode= node(data)
        if(self.head is None):
            self.head = newnode
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next= newnode

    def printsingLinkedList(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end='')
            print(temp, end='')
            print(temp.next)
            temp = temp.next
def main():
    singlyLinkedList = linkedlist()
    arr = list(map(int,input().split()))
    for i in range (len(arr)):
        singlyLinkedList.insertAtEnd(arr[i])
    singlyLinkedList.printsingLinkedList()

if __name__=='__main__':
    main()
