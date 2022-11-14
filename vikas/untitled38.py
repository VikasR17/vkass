import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('C:/Users/SPTINT-04/Desktop/vkas/pokemon.csv')
print(data[data['Name']=='charmander']['Type1'].value_counts().plot(kind='dis'))