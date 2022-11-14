import pandas as pd  
data =pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
data1 =pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
print(data, "\n\n", data1)
print(data.add(data1, fill_value=0))
print(data.sub(data1, fill_value=0))

  