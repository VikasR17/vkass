# Import pandas module using the import keyword
import pandas as pd

gvn_data = {"Names": ["Nick", "July", "Alex","Jhoo"], "Rollno": [1, 2, 3, 4], "Marks": [75, 54, 90, 86]}
rslt_datafrme = pd.DataFrame(gvn_data)
print("The above data before melting:")
print(rslt_datafrme)
print()
datafrme_meltd = pd.melt(rslt_datafrme, id_vars=["Rollno"],var_name=['nick'],value_vars=[ "Marks"])
print("The above data after melting:")
print(datafrme_meltd)