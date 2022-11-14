


import matplotlib.pyplot as pl
import seaborn as sns
import pandas as pd
data=pd.read_csv('C:/Users/SPTINT-04/Downloads/CAR DETAILS FROM CAR DEKHO.csv')
df=pd.DataFrame(data)
print(data)
sns.barplot(x='owner',y='selling_price',data=df)
sns.lineplot(x='car name',y='km_driven',data=df)
pl.show()