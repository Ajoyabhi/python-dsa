class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linklist:
    def __init__(self):
        self.head= None
        self.tail= None

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
    def insertatbegning(self,data):
        newnode = node(data)
        if(self.head is None):
            self.head = newnode
        else:
            newnode.next= self.head
            self.head = newnode
    def insertatIT(self, i, data):
        newnode= node(data)
        if(i == 0):
            self.insertatbegning(data)
        else:
            count = 0
            temp = self.head
            while(temp is not None and count is not (i-1)):
                count+=1
                temp = temp.next
            if(temp.next is None and i>count+1):
                print("invalid")
                return
            else:
                newnode.next =temp.next
                temp.next = newnode







    def printlinklist(self):
        temp= self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next
        print()

def main():
    singlelinklist = Linklist()
    singlelinklist2 = Linklist()
    arr= list(map(int,input().split()))
    for i in range(len(arr)):
        singlelinklist.insertatbegning(arr[i])
        singlelinklist2.insertatend(arr[i])
    singlelinklist2.insertatIT(3,20)

    singlelinklist.printlinklist()
    singlelinklist2.printlinklist()

if __name__=='__main__':
    main()