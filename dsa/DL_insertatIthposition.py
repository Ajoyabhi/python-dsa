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

    def insertatend(self, data):
        newnode = node(data)
        if (self.head is None):
            self.head = newnode
            self.tail = newnode
            return
        else:
            self.tail.next = newnode

            newnode.prev = self.tail
            self.tail = newnode

    # def lenghtofDLL(self,temp):
    #     if(temp is None):
    #         return 0
    #     else:
    #         return 1+ self.lenghtofDLL(temp.next)
    def lengthoflinklist(self):
        temp = self.head
        count = 0
        while(temp is not None):
            count += 1
            temp = temp.next
        return count


    def insertatIthposition(self,i,data):
        newnode = node(data)
        size = self.lengthoflinklist()
        if(i==0):
            self.insertatbegining(data)
        elif(i==size):
            self.insertatend(data)
        elif(i>size):
            print("invalid")
            return
        else:
            count = 0
            temp = self.head
            while(temp.next is not None and count is not (i-1)):
                count+=1
                temp = temp.next
            newnode.prev = temp
            newnode.next = temp.next
            temp.next.prev = newnode
            temp.next = newnode

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


    doublyLinklist.insertatIthposition(3,300)
    doublyLinklist.printDL()


if __name__ == '__main__':
    main()