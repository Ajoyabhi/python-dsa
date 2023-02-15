n, m = map(int, input().split())
k = int(input())
arr = []
for i in range (n):
    arr.append(list(map(int, input().split())))

for i in range (n):
    for j in range (m):
        arr[i][j] = (arr[i][j] * k)

for i in range (n):
    for j in range (m):
        print( arr[i][j], end=' ')
    print()

