def main():
    t = int(input())
    while (t > 0):
        n = int(input())
        if(n==0):
          print(n)
        else:
          pattern(n)
          print()
        t = t - 1

def pattern(x):
    if(x%5==0):
        if (x < 0):
            return
        print(x, end=' ')
        pattern(x - 5)
        print(x, end=' ')
    else:
        print(x, end=' ')
        if (x < 0):
            return
        pattern(x - 5)
        print(x, end=' ')

if __name__=='__main__':
    main()