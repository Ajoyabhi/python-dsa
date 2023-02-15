def main():
    t = int(input())
    while (t > 0):
        pas = input()
        fake = input()
        leftrotate(fake)
        rightrotate(fake)
        if((leftrotate(fake) == pas or rightrotate(fake)) == pas):
            print("yes")
        else:
            print("no")
        t =t-1




def leftrotate (fake):
    lf = fake[0:2]
    lr = fake[2:]
    left = lr + lf
    return left
def rightrotate (fake):
    Rr = fake[(len(fake)-2): ]
    Rl = fake[0:(len(fake)-2)]
    right = Rr + Rl
    return right

if __name__ == "__main__":
    main()
