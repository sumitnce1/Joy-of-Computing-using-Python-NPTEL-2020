list1=list(map(int,input().split()))
list2=[]
for i in list1:
  if i%5!=0:
    list2.append(i)
print(*list2,end="")