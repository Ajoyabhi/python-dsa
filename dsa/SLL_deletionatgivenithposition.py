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

    def insertatbegining(self,data):
        newnode = node(data)
        if(self.head is None):
            self.head = newnode
        else:
            newnode.next= self.head
            self.head = newnode

    def Deletionatbegining(self):
        if(self.head is None):
            return
        else:
            self.head = self.head.next

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

    def lengthoflinklist(self):
        temp = self.head
        count = 0
        while(temp is not None):
            count += 1
            temp = temp.next
        return count
    def deletionatIthposition(self,i):
        size= self.lengthoflinklist()
        if(self.head is None):
            return
        elif(i==0):
            self.Deletionatbegining()
        elif(i==size):
            self.deletionatend()
        else:
            pnt=0
            temp= self.head
            while(temp is not None and pnt!=i-1):
                pnt+=1
                temp = temp.next

            if(temp.next is None and i>pnt+1):
                print("invalid input")
                return
            else:
                temp.next = temp.next.next


    def printlinklist(self):
        temp= self.head
        while(temp is not None):
            print(temp.data, end=' ')
            temp = temp.next

def main():

    a = int(input())
    while(a>0):
        singlelinklist = Linklist()
        arr = list(map(int, input().split()))
        for i in range(len(arr)):
            singlelinklist.insertatend(arr[i])
        z = int(input())
        singlelinklist.deletionatIthposition(z)
        singlelinklist.printlinklist()
        print()
        a-=1

if __name__=='__main__':
    main()