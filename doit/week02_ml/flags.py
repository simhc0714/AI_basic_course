# -*- coding: utf-8 -*-

import urllib.request as req
local = "flags.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data"
req.urlretrieve(url, local)
print("download complete")
#%% 알고리즘 개요
'''
위 데이터 셋은 국기별 30가지 특징(나라이름, 대륙, 면적, 인구, 종교, 국기 색깔 등)을 나타내는 데이터 셋이다.
나라이름(0), zone(2), area(3), population(4)은 제외한 나머지 특징들로만 대륙을 예측하는 모델을 만들어보자.
'''
#%%
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

#%%
flag = pd.read_csv("flags.csv", header=None)
print(flag)
# 0 - 29. total 30 columns
#%%
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype
flag['Label']= flag.iloc[:,1] # column 1 = landmass

print(flag)
#%% 열 18, 29, 30만 영문 -> 숫자로 인코딩
from sklearn import preprocessing
encoder_le = preprocessing.LabelEncoder()

for i in range(5, 30, 1):
    if(is_numeric_dtype(flag.iloc[0,i]) == True):
        flag['col' + str(i)] = flag.iloc[:,i]
    else:
        flag['col' + str(i)] = encoder_le.fit_transform(flag.iloc[:,i])

print(flag)
#%%
'''
from pandas.api.types import is_numeric_dtype
print(flag.iloc[0,1])                       # 5
print(is_numeric_dtype(flag.iloc[0,1]))     # True
print("\n")
print(flag.iloc[0,28])                      # black
print(is_numeric_dtype(flag.iloc[0,28]))    # False
print("\n")
print(flag.iloc[0,27])                      # 0
print(is_numeric_dtype(flag.iloc[0,27]))    # True
print(is_string_dtype(flag.iloc[0,27]))     # False
'''
#%%
X = flag.loc[:, "col7":"col29"] # loc은 label을 기반으로 인덱싱.
y = flag["Label"]

print(X.shape, y.shape)
#%% test_size default
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

print(X_train.shape, y_train.shape) # 194*0.75 = 145.5 = 145, 23(columns)
print(X_test.shape, y_test.shape) # 194*0.25 = 48.5 = 49, 23(columns)
#%% Modelling RF
model = RandomForestClassifier()
model.fit(X_train, y_train)
#%% test data set. prediction
predict = model.predict(X_test)

print(len(predict)) # test data set에 속하는 49개 예측완료.
print(predict) # 예측한 데이터 값들
#%% train versus test
import numpy as np

print(predict == y_test.values)
print((np.sum(predict == y_test.values)) / len(predict) * 100)
# 55.10204081632652 %