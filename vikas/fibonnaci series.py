from functools import reduce
l=[0,1,1,2,3,5,8,13,21]
res1=list(map(lambda x:x-1,l))
print("add with -1",list(res1))
l1=[]
res=map(lambda l1:max(l),l)
n=set(res)
print(n)
odd=list(filter(lambda x:x%2!=0,l))
print("odd numbers in series=",odd)


print("sum of series",reduce(lambda x,y:x+y,l))
