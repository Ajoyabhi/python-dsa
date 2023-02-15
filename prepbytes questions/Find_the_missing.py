def calculate(arr, n):
    frq = [0] * (n+1)
    count = 0
    for i in range(len(arr)):
        frq[arr[i]] += 1

    for j in range(1, n + 2):
        if (frq[j] == 0):
            print(j)
            break


def main():
    x = int(input())
    while (x > 0):
        n = int(input())
        arr = list(map(int, input().split()))
        calculate(arr, n)
        x -= 1


if __name__ == '__main__':
    main()

