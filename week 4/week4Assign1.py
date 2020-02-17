list1=input()
a=list1.count('1')
b=list1.count('0')
l=len(list1)
if a==l-1 and b==1:
  print("YES",end='')
elif a==1 and b==l-1:
  print("YES",end="")
else:
  print("NO",end="")