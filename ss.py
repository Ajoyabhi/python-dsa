#x, y, z = map(int, input("Enter three values: ").split())
x,y,z=[float(i) for i in input("enter three values").split()]
print("{:.4f} is smaller than {:.2f} and {:.2f} is smaller than {:.3f}".format(x,y,y,z))
print("%.4f is smaller than %.2f and %.2f is smaller than %.3f"%(x,y,y,z))
# print("%f is smaller than %f"%(x,y))
# m=x+y+z
# print(m)