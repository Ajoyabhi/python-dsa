def main():
    t = int(input())
    while(t>0):
        n = int(input())
        maxj = -1
        mini = -1
        arr = list(map(int,input().split()))
        k = int(input())
        for i in range (n-1):
            for j in range (n):
                if(arr[i]+arr[j] > k):
                    flag = 1
                    if(maxj>j):
                        maxj = j
                    elif(maxj == j and mini > i):
                        mini = i
        if (flag == 0):
            print("no answer")
        else:
            print(mini,maxj)
        t = t-1

if __name__ == "__main__":
    main()