
def maxofrent(arr,n):
    flag=0
    for i in range(n):
        if(i==0):
            if (arr[i] > arr[i+1]):
                print(i, end=' ')
                flag = 1
        elif(i==n-1):
            if (arr[i] > arr[i -1]):
                print(n - 1, end=' ')
                flag = 1
        else:

            if ((arr[i] > arr[i - 1]) and (arr[i] > arr[i + 1])):
                print(i, end=' ')
                flag = 1
    if(flag==0):
        print(-1)
    print()

def main():
    x = int(input())
    while(x>0):
        n = int(input())
        arr = list(map(int,input().split()))
        maxofrent(arr,n)
        x =x-1
if __name__=='__main__':
    main()
