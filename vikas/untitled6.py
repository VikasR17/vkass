

import pandas as pd
import numpy as np
# creating a dataframe
dict = pd.DataFrame({'Fiest name': ['aryan', 'rohan', 'riya','yash','siddanth'],
      'last name': ['singh', 'agarwal', 'shah','bathia','khnna'],
      'Type':['Full time employe','Intern','Full time employe','Part time employe','Full time employe'],
      'Department':['Administration','Technical','Administration','Technical','Management'],
      'YOE': [2,3,5,7,6],
      'Salary':[20000,5000,10000,10000,20000]})

df=pd.DataFrame(dict)
print(df)
pivot=pd.pivot_table(df,index=['Type','Department'],values=['Salary'],aggfunc=np.mean)
print(pivot)
pivot1=pd.pivot_table(df,index=['Type','Department'],values=['Salary'],aggfunc=[np.sum,np.mean,pd.Series.nunique])
print(pivot1)
