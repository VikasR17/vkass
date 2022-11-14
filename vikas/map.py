import pandas as pd
df=pd.DataFrame([[40,18,25,100],[52,47,89,99],[25,2,36,99]],columns=['maths','science','cse','ece'])
print(df)
a=df.min()
print(a)
a=df.maths.sum()
print(a)
a=df.groupby("cse")

print(df.agg(['sum','min','max']))

