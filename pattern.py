ch = input()
s= 8
for i in range (1,6):
  for m in range (1, i+1):
   print(m, end='')
  for k in range (0,s):
   print(" ",end='')
  s=s-2
  for j in range (i,0,-1):
   print(j, end='')
  print()