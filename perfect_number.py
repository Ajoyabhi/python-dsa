def main():
    n = int(input())
    while(n>0):
        x = int(input())
        count = 0
        for i in range(1,x):
            if(x%i ==0):
                count+=i
        if(count==x):
            print("true")
        else:
            print("false")
        n = n-1

if __name__=='__main__':
    main()

