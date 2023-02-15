def mergesort(arr, l, r):
    if (l < r):
        mid = l + (r - l) // 2
        mergesort(arr, l, mid)
        mergesort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    n = mid - l + 1
    m = r - mid
    arr1 = [0] * n
    arr2 = [0] * m
    for i in range(n):
        arr1[i] = arr[l + i]
    for i in range(m):
        arr2[i] = arr[mid + 1 + i]
    i = 0
    j = 0
    k = l
    while (i < n and j < m):
        if (arr1[i] < arr2[j]):
            arr[k] = arr1[i]
            i += 1
            k += 1
        else:
            arr[k] = arr2[j]
            j += 1
            k += 1
    while (i < n):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while (i < m):
        arr[k] = arr2[j]
        j += 1
        k += 1


from sys import setrecursionlimit

setrecursionlimit(10000000)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    mergesort(arr, 0, n - 1)
    for i in range (n):
        print(arr[i],end=' ')
    print()

if __name__ == '__main__':
    main()
