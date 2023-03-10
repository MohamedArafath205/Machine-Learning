# -*- coding: utf-8 -*-
"""Major Project 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pYBZRDqxyfWv6_X0aIUKM3Sr_OtbQiHF
"""

import pandas as pd
df = pd.read_csv('/content/train.csv')
df

df.head()

df.tail()

df.shape

df.describe()

df.columns

df.nunique()

df['Embarked'].unique()

df.isnull().sum()

df = df.drop(['PassengerId', 'Name', 'Ticket', 'Embarked'], axis=1)
df.head()

corelation = df.corr()

import seaborn as sns
sns.heatmap(corelation, xticklabels=corelation.columns, yticklabels=corelation.columns, annot=True)

sns.pairplot(df)

sns.relplot(x='Survived', y='Fare', hue='Sex', data=df)

sns.distplot(df['Pclass'])

sns.barplot(x='Sex', y='Survived', data=df)

sns.barplot(x='Sex', y='Survived', hue='Pclass', data=df)

df.info()