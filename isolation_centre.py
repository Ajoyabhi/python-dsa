def main():
    t = int(input())
    while(t>0):
        n,m = map(int, input().split())
        str = input()
        freq = [0]*26
        for ele in str:
            freq[ord(ele)-97] +=1
        for i in range (m):
            q = int(input())
            count = 0
            for j in range (26):
              if (freq[i]>q):
                    count = freq[i]-q
            print(count)
    t = t-1
if __name__ == "__main__":
    main()


