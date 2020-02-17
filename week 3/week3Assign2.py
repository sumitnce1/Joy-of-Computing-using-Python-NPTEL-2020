list1=list(map(int,input().split()))
list1.sort()
length=len(list1)
print(list1[length-2],list1[1],end="")