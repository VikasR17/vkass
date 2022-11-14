import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
train=pd.read_csv('‪C:/Users/SPTINT-04/Downloads/train.csv')
print(train.head())
sns.countplot(x='Survived', hue='Pclass', data= train)