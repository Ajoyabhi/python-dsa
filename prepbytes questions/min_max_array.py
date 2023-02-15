import sys
def minmaxarray(arr,n):
    min = sys.maxsize
    max = -1
    for i in range(n):
        if(min>arr[i]):
            min = arr[i]
        if(max<arr[i]):
            max = arr[i]
    print(max, min)
def main():
    x = int(input())
    while(x>0):
        n = int(input())
        arr = list(map(int,input().split()))
        minmaxarray(arr,n)
        x =x-1
if __name__=='__main__':
    main()
