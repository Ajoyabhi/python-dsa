def getunique(arr):
    resDict = {}
    for ele in arr:
        if ele in arr:
            resDict[ele] += 1
        else:
            resDict[ele] = 1
    arrTemp = []
    for ele in resDict:
        if resDict[ele] == 1
            arrTemp.append(ele)
    print(len(arrTemp))
count = input()
arr = list(map(int, input().split()))
getunique(arr)