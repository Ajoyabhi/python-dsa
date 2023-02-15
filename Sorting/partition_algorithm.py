def Quicksort(arr,l,r):
    if(l<r):
        P = partition(arr,l,r)
        Quicksort(arr,l,P-1)
        Quicksort(arr,P+1,r)

def partition(arr ,low,high):
    x= arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<=x:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        Quicksort(arr,0,n-1)
        for i in range(n):
            print(arr[i], end=' ')
        print()
        t= t-1

if __name__ == '__main__':
    main()



