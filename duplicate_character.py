t = int(input())
while(t>0):
    str = input()
    frq = [0]*26
    for i in range (len(str)):
        frq[ord(str[i])-97] += 1
    flag = 0
    for i in range (0,26):
        if(frq[i]>1):
            print('{}={}'.format(chr(i+97),frq[i],end=' '))
            flag = 1
    if (flag == 0):
        print("-1")
    else:
        print()
    t=t-1



