import sys
def minimumrent(arr,n):
    min = sys.maxsize
    index = 0
    for i in range(n):
        if(min>arr[i]):
            min = arr[i]
            index = i
    return index
def main():
    x = int(input())
    while(x>0):
        n = int(input())
        arr = list(map(int,input().split()))
        print(minimumrent(arr,n))
        x =x-1
if __name__=='__main__':
    main()
