n = int(input())
for i in range n:
  x = int(input())
  while(x>0):
   rem = x%10
   x = x//10
  print("first digit of integer is", rem)
