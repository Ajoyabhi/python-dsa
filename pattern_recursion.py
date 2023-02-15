def main():
  t=int(input())
  while(t>0):
    n=int(input())
    pattern(n)
    t=t-1
def pattern (n):
    if(n>0):
        print(n)
        pattern(n-5)
    if(n<0):
        print(n)
        pattern(n+5)
    if(n==n):
        return

if __name__=='__main__':
    main()