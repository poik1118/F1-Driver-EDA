# https://www.kaggle.com/datasets/petalme/f1-drivers-dataset
# https://www.kaggle.com/code/xokent/f1-drivers-eda
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os, sys

#%%
data = pd.read_csv('/workspaces/F1-Driver-EDA/dataset/F1Drivers_Dataset.csv').fillna('Non')
data.head()

# %%
data.Seasons.nunique()

#%%
data.dtypes

#%%
ax = sns.countplot(data=data, y='Nationality', order = data['Nationality'].value_counts().index)
for label in ax.containers:
    ax.bar_label(label)
plt.gcf().set_size_inches(10, 10)
plt.title('Nationality counting')
plt.xlabel('Count')
plt.ylabel('Nationality')
plt.show()

# %%
nationality = data.groupby('Nationality')[['Championships', 'Race_Entries', 'Race_Starts', 'Pole_Positions', 'Race_Wins', 'Podiums']].sum()

# Create a barplot of podiums and championships
plt.figure(figsize=(10,8))
plt.barh(nationality.index, nationality['Podiums'], label='Podium', color='green')
plt.barh(nationality.index, nationality['Championships'], label='Championship', color='red')

plt.legend(loc='best')
# Set xlabel to nationality
plt.xlabel('Podiums & Championships')
plt.title('Barplot Podiums & Championships each nationality')
plt.show()

# %%
sns.scatterplot(data=nationality, x='Podiums', y='Championships', color='black')
plt.title('Podiums vs Championships')
plt.show()

# %%
plt.figure(figsize=(10, 8))
ax = sns.barplot(data=nationality, y=nationality.index, x='Pole_Positions')
for label in ax.containers:
    ax.bar_label(label)
plt.show()

#%%
def barplot(col,col1,datas,cr,color):
    sns.barplot(x=col, y=col1 ,data=datas,hue=cr, palette=color)
    plt.show()
barplot('Nationality','Points',data,'Decade', 'plasma')

# %%
max_champs = data.Championships.max()
data.query('Championships == {}'.format(max_champs))

# %%
# 데이터들의 통계량을 요약.
data.describe()
# %%
# round : 숫자데이터를 반올림 (NULL : 0, 1 : 소숫점 첫번째 ...)
data.describe().round()
# %%
# include : 해당 타입이 포함된 값을 출력
data.describe(include='all').round(1)
# %%
# 'O' : String 문자열 타입
data.describe(include='O')
#%%
data.describe(exclude='O')

#%%

# %%
# hist : 히스토그램 (도수분포표 그래프)
data.select_dtypes(exclude='O').hist(figsize=(11,9));

# %%
