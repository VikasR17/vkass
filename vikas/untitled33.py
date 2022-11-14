# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 02:48:40 2022

@author: SPTINT-04
"""
import matplotlib.pyplot as pl
import seaborn as sns
import pandas as pd
df=pd.read_csv("C:/Users/SPTINT-04/Downloads/Internet Speed 2022.csv")
sns.barplot(x='Countries',y='mobile',data=df)
