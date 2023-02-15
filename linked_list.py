class node:
    def __init__(self,data):
        self.data = data
        self.next = None

x= node(20)
y= node(10)
print(x)
print(y)
print(x.next)
x.next = y
print(x.next)
print(y.next)
print(x.next.data)
print(x.data)