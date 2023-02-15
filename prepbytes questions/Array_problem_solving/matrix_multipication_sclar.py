def multiplyScalar(arr,m,n,k):
    for i in range(m):
        for j in range(n):
            arr[i][j]*=k
    for k in range(m):
        for l in range(n):
            print(arr[k][l],end=' ')
        print()



def main():
    m,n,k = map(int,input().split())
    arr=[]
    for i in range(m):
        arr.append(list(map(int,input().split())))
    multiplyScalar(arr,m,n,k)


if __name__ == '__main__':
    main()

