a,b=input().split(" ")
a=int(a)
b=int(b)
mat=[[0 for i in range(b)]for j in range(a)]
val=1
for i in range(a):
  for j in range(b):
    mat[i][j]=val
    val=val+1
for i in range(a):
  for j in range(b):
    if j!=(b-1):
      print(mat[i][j],end=" ")
    else:
      print(mat[i][j],end="")
  if i!=(a-1):
    print()