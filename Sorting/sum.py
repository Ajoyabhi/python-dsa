def digitSum(x):
    sum=0
    while(x>0):
        sum += x%10
        x=x//10
    return sum

def main():
    x = int(input())
    y = digitSum(x)
    if(y>9):
        y = digitSum(y)
    print(y)

if __name__ == '__main__':
    main()