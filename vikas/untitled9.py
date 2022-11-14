import pandas as pd
a=pd.Series([1,2,3,4,5])
b=pd.Series([6,7,8,4,10])
print("series in a")
print(a)
print("series in b")
print(b)
res=a.isin(b)
print(res)