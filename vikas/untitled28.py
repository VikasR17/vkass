import seaborn as sns

df = sns.load_dataset('tips')

sns.boxplot(x='day', y='total_bill', data=df, hue='smoker')
