import pandas as pd
  
# creating a dataframe
df = pd.DataFrame({'A': ['vinay', 'vikas', 'varsh'],
      'B': ['Masters', 'Graduate', 'Graduate'],
      'C': [27, 23, 21]})
  
a=df.pivot('A', 'B', 'C')
print(a)
b=df.pivot(index ='A', columns ='B', values =['C', 'A'])
print(b)