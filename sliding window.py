def main ():
    t = int(input())
    while(t>0):
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))
        summax(arr, n, k)
        t= t-1

def summax(arr, n , k):
    sum=0
    max=-1
    for i in range (0,k):
        sum = arr[i]
    max = sum
    for j in range (k, n-1):
        sum = sum - arr[j-k] + arr[j]
        if(sum>max):
            max = sum
    print(max)


if __name__ == "__main__":
    main()
