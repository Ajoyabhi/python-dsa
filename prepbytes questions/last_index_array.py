def lastindex(arr,n):
    l=-1
    for i in range(n):
        if(arr[i]==1):
            l = i
    return l

def main():
    x = int(input())
    while(x>0):
        n = int(input())
        arr = list(map(int,input().split()))
        print(lastindex(arr,n))
        x = x-1

if __name__ =='__main__':
    main()

