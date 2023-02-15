def main():
    bob = list(map(int, input().split()))
    alice = list(map(int, input().split()))
    award = [0]*2
    for i in range (3):
        if(bob[i]>alice[i]):
            award[1]+=1
        elif(bob[i]<alice[i]):
            award[0]+=1
        else:
            continue
    for j in range (len(award)):
        print(award[j], end=' ')

if __name__ == '__main__':
    main()