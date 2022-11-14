import pandas as pd
df=pd.DataFrame(((17,'vikas',8000),(18,'vnay',5000)),columns=['id','name','salary'])
print(df)
p=df.salary.agg(('min','max','sum'))
print(p)
