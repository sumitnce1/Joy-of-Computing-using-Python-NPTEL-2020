N=int(input())
A=[int(i) for i in input().split(" ")]
B=[]
for i in range(len(A)-1,-1,-1):
  B.append(A[i])
C=[]
for i in range(len(B)):
  C.append(A[i]+B[i])
for i in range(len(C)):
  if(i==len(C)-1):
    print(C[i],end="")
  else:
    print(C[i],end=" ")