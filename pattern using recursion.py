def main():
    n= int(input())
    pattern(n,1)

def pattern(n,i):
    if(n==0):
        return
    printn(i)
    print("\n",end='')
    pattern(n-1,i+1)
def printn(i):
    if(i==0):
        return
    print("*",end=' ')
    printn(i-1)

if __name__=='__main__':
    main()
