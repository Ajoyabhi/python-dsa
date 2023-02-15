def mergesort(arr, l, r):
    if (l < r):
        mid = l + (r - l) // 2
        mergesort(arr, l, mid)
        mergesort(arr, mid + 1, r)
        merge(arr, l, r, mid)


def merge(arr, l, r, mid):
    n = mid - l + 1
    m = r - mid
    arr1 = [0] * n
    arr2 = [0] * m
    for i in range(n):
        arr1[i] = arr[l + i]
    for i in range(m):
        arr2[i] = arr[mid + i + 1]
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
        k += 1
        i += 1
    while (j < m):
        arr[k] = arr2[j]
        k += 1
        j += 1


def main():
    t = int(input())
    while (t > 0):
        n = int(input())
        arr = list(map(int, input().split()))
        arr1=arr.copy()
        mergesort(arr, 0, n - 1)
        count=0
        for i in range(n):
          if (arr1[i] != arr[i]):
            count += 1
        print(count)

        t = t-1
if __name__=='__main__':
    main()