class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linklist:
    def __init__(self):
        self.head= None

    def insertatbegining(self,data):
        newnode = node(data)
        if(self.head is None):
            self.head = newnode
        else:
            newnode.next= self.head
            self.head = newnode

    def printlinklist(self):
        temp= self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next

def main():
    singlelinklist = Linklist()
    arr= list(map(int,input().split()))
    for i in range(len(arr)):
        singlelinklist.insertatbegining(arr[i])
    singlelinklist.printlinklist()

if __name__=='__main__':
    main()