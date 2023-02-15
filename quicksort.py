def quicksort(arr, l, r):
  if l < r:
    p = partion(arr, l, r)
    quicksort(arr, l, p - 1)
    quicksort(arr, p + 1, r)


def partion(arr, l, r):
  x = arr[r]
  i = l - 1
  for j in range(r):
    if (arr[j] < x):
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[r] = arr[r], arr[i + 1]
  return i + 1


def main():
  t = int(input())
  while (t > 0):
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = arr.copy()
    count = 0
    quicksort(arr, 0, n - 1)
    for i in range(n):
      print(arr[i], end=' ')
    print()
    for i in range(n):
      if (arr1[i] != arr[i]):
        count += 1

    print(count)
    t = t - 1


if __name__ == '__main__':
    main()