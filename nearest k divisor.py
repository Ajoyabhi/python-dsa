import math
import sys
def main():
    n = int(input())
    q = int(input())
    arr  = []
    for i in range (1, int(math.sqrt(n))+1):
        if(n%i==0):
           arr.append(i)
        if(n//i != i):
            arr.append(n//i)
    arr.sort()
    while(q>0):
        k = int(input())
        low=0
        high= len(arr)
        mid= (low+high)//2
        flag=0
        while(low<high and flag==0):
            if(arr[0]>k):
                print(arr[0])
                flag=1
            elif(arr[len(arr)-1]<k):
                print(arr[len(arr)-1])
                flag=1
            elif(arr[mid]==k):
                print(arr[mid])
                flag=1
            else:
                if(k>arr[mid]):
                    if(k<arr[len(arr)-1] and k<arr[mid+1]):
                        if(abs(k-arr[mid])>abs(k-arr[mid+1])):
                            print(arr[mid+1])
                            flag=1
                        else:
                            print(arr[mid])
                            flag = 1
                    else:
                        low = mid+1
                if(k<arr[mid]):
                    if(k>arr[0] and k>arr[mid-1]):
                        if(abs(k-arr[mid])>abs(k-arr[mid-1])):
                            print(arr[mid-1])
                            flag = 1
                        else:
                            print(arr[mid])
                            flag = 1
                    else:
                        high = mid-1
            if(flag==0):
                print(arr[mid])
    q = q-1

if __name__ =='__main__':
    main()













