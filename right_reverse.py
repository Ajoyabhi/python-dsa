def main():
    t = int(input())
    while (t > 0):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        reverseRAlgo(arr, n - k, n - 1)
        reverseRAlgo(arr, 0, n - k - 1)
        reverseRAlgo(arr, 0, n - 1)
        showarr(arr, n)
        t = t - 1
def reverseRAlgo(arr, i, j):
    while (i < j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1


def showarr(arr, n):
    for i in range(n):
        print(arr[i], end=' ')



if __name__ == "__main__":
    main()


