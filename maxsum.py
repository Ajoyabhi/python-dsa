def main ():
    t = int(input())
    while(t>0):
        n,k = map(int, input().split())
        arr = list(map(int, input().split()))
        summax(arr, n, k)
        t= t-1

def summax(arr,n,k):
    max = 0
    for i in range (0, n-k):
        sum = 0
        for j in range (i, i+k):
            sum += arr[j]
        if (sum > max):
            max = sum
    print(max)

if __name__ == "__main__":
    main()
