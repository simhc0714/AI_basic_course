# -*- coding: utf-8 -*-
#%% 라이브러리 불러오기
import sys
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import seaborn as sns

#%% 데이터 준비
from sklearn.datasets import load_iris

iris = load_iris()

# iris 데이터 -- 딕셔너리 (키:값)
# print(iris.key())
# dict_keys(['data', 'target', 'frame', 'target_names',
# 'DESCR', 'feature_names', 'filename'])

# 'data' : 꽃잎의 너비-길이, 꽃받침의 너비-길이 (4개 변수, 피쳐) : 150개
# 'feature_names' : data의 값이 갖는 이름
# ['sepal length(cm)', 'sepal width(cm)', 'petal length(cm)', 'petal width(cm)']


#%% iris 데이터 셋의 행렬확인
print( iris['data'].shape )
print( iris['feature_names'])
print( iris['data'][:5])      # 5개의 데이터 확인
print( iris['target_names'][:5]) 
print( iris['target'][:5]) 

#%% iris 데이터 셋의 크기(행-열)
print(type(iris['target']))

print(iris['target'].shape)     # 1차원 배열
print(iris['data'].shape)       # 2차원 배열

# X_train : (60000, 28, 28)     # 3차원 배열
# 동영상 데이터 (__, 28, 28, 60) # 4차원 배열

#%% 데이터를 나누기

# train.csv, test.csv
# train: 학습(머신에 공부시킬 데이터)
# test: 예측을 위한 데이터
# 총 150개의 iris데이터(data, target)를 적절한 비율로 나눠준다.
# 학습용, 테스트용

#%%
from sklearn.model_selection import train_test_split
# train_test_split(입력, 출력)

all_X = iris['data']
all_y = iris['target']

X_train, X_test, y_train, y_test = train_test_split(all_X, all_y, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#%% 모델 선택, 모델 학습, 모델을 이용한 예측, 평가
from sklearn.neighbors import KNeighborsClassifier

# model selection
knn = KNeighborsClassifier()

# model learning
knn.fit(X_train, y_train)

# Forecast data using with model 'knn'
# [model].predict(input_test)
pred = knn.predict(X_test)
pred

#%% Evaluation - Original Answer is 'y_test'.
# be compared 'y_test' with 'pred'
print(sum(pred==y_test)/len(pred))

#%% 추가 실습
# Titanic 데이터 셋을 활용하여 knn 모델을 구현해보자