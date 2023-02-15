class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linklist:
    def __init__(self):
        self.head= None
        self.tail = None

    def insertatend(self,data):
        newnode = node(data)
        if(self.head is None):
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode




    def printlinklist(self):
        temp= self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next

def main():
    singlelinklist = Linklist()
    arr= list(map(int,input().split()))
    for i in range(len(arr)):
        singlelinklist.insertatend(arr[i])
    singlelinklist.printlinklist()

if __name__=='__main__':
    main()