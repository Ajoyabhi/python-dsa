def evenodd(arr, n):
    arr1 = []
    arr2 = []
    for i in range(len(arr)):
        if (arr[i] % 2 == 0):
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])

    if (((len(arr1) == 0) or (len(arr2) == 0))):
        print("ivalid input")
        return

    for j in range(len(arr1)):
        print(arr1[j], end=' ')

    print()

    for k in range(len(arr2)):
        print(arr2[k], end=' ')
    print()


def main():
    x = int(input())
    while (x > 0):
        n = int(input())
        arr = list(map(int, input().split()))
        evenodd(arr, n)
        x -= 1


if __name__ == '__main__':
    main()