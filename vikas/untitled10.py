import pandas as pd
reviews = pd.read_csv('‪C:/Users/SPTINT-04/Downloads/train.csv', index_col=0)
import seaborn as sns
sns.countplot(reviews['Survived'])