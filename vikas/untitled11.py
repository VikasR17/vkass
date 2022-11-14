
import pandas as pd

df = pd.DataFrame(((17,'vikas',100000),(18,'vinay',50000),(19,'hemanth',500)),columns=['id','name','salary'])

print(df)

df1=df.pivot('id', 'salary', 'name')
print(df1)

a=df.salary.agg(('sum','max','min','average'))
print(a)
d=df.melt()
print(d)
 
v=df.pivot(('name','id','salary'))
print(v)