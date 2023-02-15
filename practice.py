import sys
def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    frq = [0] * n
    if(n==1):
        print(n)
    else:
        for i in range(0, n):
            frq[arr[i]] += 1
        mi = sys.maxsize
        for i in range(0, n):
            if (k == frq[i]):
                if (i < mi):
                    mi = i
        print(mi)
if __name__ =='__main__':
     main()
