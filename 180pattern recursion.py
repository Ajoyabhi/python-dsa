def main():
    n=int(input())
    pattern(n,n)

def pattern(n,num):
    if(n==0):
        return
    print_spaces(n-1)
    print_astrick(num-n+1)
    print()
    pattern(n-1,num)

def print_spaces(spaces):
    if(spaces==0):
        return
    print(" ",end=' ')
    print_spaces(spaces-1)

def print_astrick(astrick):
    if(astrick==0):
        return
    print("*",end=' ')
    print_astrick(astrick-1)

if __name__=='__main__':
    main()