s = ['a','b','c','d','e']

def stringMultiply(x):
    return 2*x

z = [stringMultiply(s[x]) for x in range(len(s)-1, -1, -1)]

`
print(z)