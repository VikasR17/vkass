# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:04:27 2022

@author: SPTINT-04
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('C:/Users/SPTINT-04/Desktop/TRAIN/train.csv')
#g=sns.countplot(x='Sex',hue='Survived',data=data)
#g=sns.countplot(x='Embarked',hue='Survived',data=data)
#g=sns.countplot(x='Embarked',hue='Pclass',data=data)
#g=sns.countplot(x='Pclass',hue='Survived',data=data)
def add_family(df):
    df['FamilySize']=df['SibSp']+df['Parch']+1
    return df
data=add_family(data)
print(data.head(10))
#g=sns.countplot(x='FamilySize',hue='Survived',data=data)
#g=sns.catplot(x="FamilySize",
#hue="Survived",col="Sex",data=data,kind="count",height=4,aspect=.7);
#g=sns.catplot(x="Pclass",
#hue="Sex",col="Survived",data=data,kind="count",height=4,aspect=.7);
#g=sns.catplot(x="Embarked", hue="Sex", col="Survived", data=data, kind="count",height=4,aspect=.7)


g=sns.displot(x="Embarked", hue="Sex", col="Survived",data=data, kind="hist", height=4,aspect=.7)
              