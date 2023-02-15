#program for finding the first non repetive character is the string
def countrepetive(str):
    resUnseen = []
    resSeen = []
    for ele in str:
        if ele in resUnseen:
            resSeen.append(ele)
            resUnseen.remove(ele)
        elif ele in resSeen:
            continue
        else:
            resUnseen.append(ele)
    if resUnseen:
        return(str.find(resUnseen[0]))
    else:
        return -1

for _ in range (int(input())):
    print(countrepetive(input()))