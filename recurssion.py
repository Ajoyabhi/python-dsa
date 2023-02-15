def main():
    t = int(input())
    while (t > 0):
        n = int(input())
        x = sum(n)
        print(x)
        t = t - 1

from sys import setrecursionlimit
setrecursionlimit(1000000000)
def sum(n):
    if (n ==0 or n==1):
        return n
    return n + sum(n - 1)


if __name__ == '__main__':
    main()