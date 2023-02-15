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