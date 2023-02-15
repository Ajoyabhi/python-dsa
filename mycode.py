import sys

def search(arr,f,l,target):
    if (f<l):
        return -1
    if(arr[f]==target):
        return f
    if(arr[l]==target):
        return l
    return search(arr,f+1,l-1,target)

def main():
    arr = [1,2,3,6,8,10]
    l= len(arr)
    target = 3
    print(search(arr,0,l-1,target))
from sys import setrecursionlimit
setrecursionlimit(10000000)
if __name__ == '__main__':
    main()



