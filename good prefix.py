def main():
    t = int(input())
    k, x = map(int, input().split())
    str = input()
    count=0
    freq = [0]*26
    for ele in str:
        freq[ord(ele)-97] +=1
    for i in range(26):
        if(freq[i]>x):
            if(k>0):
                freq[i] -= 1
            else:
                break
        else:
            count +=1
    print(count)
    t=t-1

if __name__ == '__main__':
    main()
