def uppertriangular(mat1,m,n):
    mat2=[]
    for k in range(m):
        mat2.append([0] * n)
    for i in range(m):
        for j in range(n):
            if(i>=j):
                mat2[i][j]=mat1[i][j]
            else:
                mat2[i][j]=0
    for i in range(m):
        for j in range(n):
            print(mat2[i][j],end=' ')
        print()

def lowertriangular(mat1,m,n):
    mat3 = []
    for k in range(m):
        mat3.append([0] * n)
    for i in range(m):
        for j in range(n):
            if (j >= i):
                mat3[i][j] = mat1[i][j]
            else:
                mat3[i][j] = 0
    for i in range(m):
        for j in range(n):
            print(mat3[i][j], end=' ')
        print()

def main():
    m,n = map(int,input().split())
    mat1=[]
    for i in range(m):
        mat1.append(list(map(int,input().split())))
    uppertriangular(mat1,n,m)
    lowertriangular(mat1,m,n)




if __name__ == '__main__':
    main()

