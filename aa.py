def mergesort(arr, l, r):
    if (l < r):
        mid = l + (r - l) // 2
        mergesort(arr, l, mid)
        mergesort(arr, mid + 1, r)
        merge(arr, l, r, mid)


def merge(arr, l, r, mid):
    n = mid + 1 - l
    m = r - mid
    arr1 = [0] * n
    arr2 = [0] * m
    for i in range(n):
        arr1[i] = arr[l+i]
    for i in range(m):
        arr2[i] = arr[mid+1+i]
    i = 0
    j = 0
    k = l
    while (i < n and j < m):
        if (arr1[i] < arr2[j]):
            arr[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr[k] = arr2[j]
            k = k + 1
            j = j + 1
    while (i < n):
        arr[k] = arr1[i]
        k = k + 1
        i = i + 1
    while (j < m):
        arr[k] = arr2[j]
        k = k + 1
        j = j + 1


def main():
    t = int(input())
    while (t > 0):
        x = int(input())
        arr=[int(i) for i in str(x)]
        n = len(arr)
        mergesort(arr, 0, n - 1)
        count=0
        for i in range(n-1):
            if (arr[i + 1] - arr[i] == 1):
                count+=1
            else:
                break
        if (count==(n-1)):
            print("YES")
        else:
            print("NO")
        t = t - 1


if __name__ == '__main__':
    main()