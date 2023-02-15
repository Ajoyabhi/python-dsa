class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linklist:
    def __init__(self):
        self.head= None

    def insertatend(self,data):
        newnode = node(data)
        if(self.head is None):
            self.head = newnode
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
                # print("Abhishek")
            temp.next = newnode

    def deletionatend(self):
        if(self.head is None):
            return
        elif(self.head.next is None):
            self.head = None
        else:
            sl = self.head
            while(sl.next.next is not None):
                sl = sl.next
            self.tail = sl
            sl.next = None


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
    singlelinklist.deletionatend()
    singlelinklist.printlinklist()

if __name__=='__main__':
    main()