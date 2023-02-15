def additionMat(mat1,mat2,mat3,m,n):
    for i in range(m):
        for j in range(n):
            mat3[i][j] =mat1[i][j] +mat2[i][j]

    for i in range(m):
        for j in range(n):
            print(mat3[i][j],end=' ')
        print()



def multiplyMat(mat1, mat2,mat4, m, n):
    for i in range(m):
        for j in range(n):
            for k in range(n):
                mat4[i][j] = mat4[i][j] + (mat1[i][k] * mat2[k][j])

    for i in range(m):
        for j in range(n):
            print(mat4[i][j], end=' ')
        print()

def main():
    m,n = map(int,input().split())
    mat1=[]
    mat2=[]
    for i in range(m):
        mat1.append(list(map(int,input().split())))
    for j in range(m):
        mat2.append(list(map(int, input().split())))
    mat3 = []
    mat4 = []
    for k in range(m):
        mat3.append([0] * n)
    for l in range(m):
        mat4.append([0] * n)

    additionMat(mat1,mat2,mat3,m,n)
    multiplyMat(mat1,mat2,mat4,m,n)



if __name__ == '__main__':
    main()

