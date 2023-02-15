def mergesort(arr,low,high):
    if(low<high):
        mid = (low+(high-low))//2
        mergesort(arr,low,mid)
        mergesort(arr, mid+1, high)
        merge(arr,low,mid,high)


def merge(arr,low,mid,high):
    n = mid-low+1
    m= high-mid
    arr1 = [0]*n
    arr2 = [0]*m
    for i in range (n):
        arr1[i] = arr[low + i]
    for j in range(m):
        arr2[j] = arr[mid+1+j]

    i = 0
    j = 0
    k = low

    while(i<n and j<m):
        if(arr1[i]<arr2[j]):
            arr[k] = arr1[i]

            k = k+1
            i = i+1
        else:
            arr[k]= arr2[j]

            k = k+1
            j= j+1

    while(i<n):
        arr[k]=arr1[i]
        k+=1
        i+=1

    while(i<m):
        arr[k]=arr2[j]
        k+=1
        j+=1

from sys import setrecursionlimit

setrecursionlimit(10000000)

def main():
    t = int(input())
    while(t>0):
        n = int(input())
        arr = list(map(int, input().split()))
        mergesort(arr,0,n-1)
        for i in range(n):
            print(arr[i], end=' ')
        print()
        t= t-1

if __name__ == '__main__':
    main()