def main():
    t = int(input())
    while(t > 0):
        n = int(input())
        arr = list(map(int,input().split()))
        flag = True
        for i in range(n-1):
            if(arr[i] < arr[i+1]):
                continue
            else:
                flag = False
        if(flag):
            print(n)
        else:
            c = [0]*1
            mergesort(arr, 0, n-1, c)
            print(c[0]+1)

def mergesort(arr,l,r,c):
    if(l<r):
        mid=l+(r-l)//2
        mergesort(arr,0,mid,c)
        mergesort(arr,mid+1,r,c)
        merge(arr,l,r,mid,c)

def merge(arr,l,r,mid,c):
    n=mid+1-l
    m=r-mid
    arr1=[0]*n
    arr2=[0]*m
    for i in range(n):
        arr1[i]=arr[l+i]
    for j in range(m):
        arr2[j]=arr[mid+1+j]
    i=0
    j=0
    c1=0
    while(i<n-1):
        if(arr1[i]<=arr1[i+1]):
            i+=1
            c1+=1
        else:
            break
    if(c1+1==n):
        if(c1>c[0]):
            c[0]=c1
    c2=0
    while(j<m-1):
        if(arr2[j]<=arr2[j+1]):
            j+=1
            c2+=1
        else:
            break
    if(c2+1==m):
        if(c2>c[0]):
            c[0]=c2
from sys import setrecursionlimit
setrecursionlimit(10000000)

if __name__=='__main__':
    main()

