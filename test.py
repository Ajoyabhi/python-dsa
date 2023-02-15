def main():
    t = int(input())
    while (t > 0):
        n = int(input())
        x = n % 8
        m = n//8
        if (x == 1 or x == 4):
            if (x == 1):
                print("%dLB"%(n+3))
            else:
                print("%dLB"%(n-3))
        elif (x == 2 or x == 5):
            if (x == 2):
                print("%dMB"%(n+3))
            else:
                print("%dMB"%(n-3))
        elif (x == 3 or x == 6):
            if (x == 3):
                print("%dUB"%(n+3))
            else:
                print("%dUB"%(n-3))
        else:
            if (x == 7):
                print("%dSU"%(n+1))
            else:
                print("%dSL"%(n-1))
        t -= 1


if __name__ == '__main__':
    main()

