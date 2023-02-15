class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtend(self, data):
        newnode = Node(data)
        if (self.head is None):
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode

    def lenghtofLL(self):
        temp = self.head
        count = 1
        while (temp.next is not None):
            count += 1
            temp = temp.next
        return count

    def printmiddleElement(self):
        len = self.lenghtofLL()
        # if (len % 2 == 0):
        #     len -= 1

        middle = len // 2
        # print(mid)
        temp = self.head

        while (middle > 0):
            temp = temp.next
            middle -= 1
        print(temp.data)


def main():
    x = int(input())
    while (x > 0):
        ll = linklist()
        y = int(input())
        arr = list(map(int, input().split()))
        for i in range(len(arr)):
            ll.insertAtend(arr[i])
        ll.printmiddleElement()


if __name__ == '__main__':
    main()





