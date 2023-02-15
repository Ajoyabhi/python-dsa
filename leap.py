def main():
    t = int(input())
    if ((t % 4 == 0 and t % 100 != 0) or (t % 400 == 0)):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()