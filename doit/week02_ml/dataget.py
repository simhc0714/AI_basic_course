# 2020-09-29 (화) 수업
# 웹사이트에서 데이터 긁어오기

# 버섯 데이터를 가지고 머신러닝 모델을 만들고 학습한 모델을 이용하여
# 새로운 데이터의 독이 있는지 없는지 예측을 해보자!
# (1) 75%는 학습 데이터 셋, (2) 25%는 테스트 데이터 셋

#%% 데이터 수집
# 온라인에서 다운로드하기!
import urllib.request as req
local = "mushroom.csv" #쉼표로 구분하는 데이터형
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)
print("download complete")

#%% 모델 생성
import pandas as pd # 데이터 불러오기, 처리
from sklearn.ensemble import RandomForestClassifier # 랜덤포레스트 메서드
from sklearn import metrics # 학습데이터 셋을 평가하는 지표
from sklearn.model_selection import train_test_split

#%% 데이터 읽기
mush = pd.read_csv("mushroom.csv", header=None) # 제목이 없으면 header=None으로 설정.
print(mush)

#%% 랜덤포레트는 숫자로 input을 줘야지 이해하기 때문에 데이터를 숫자로 변경하는 작업.
from sklearn import preprocessing

# preprocessing 모듈 안의 LabelEncoder 라는 함수를 불러옵니다.
encoder_le = preprocessing.LabelEncoder()

# 첫번째 열을 숫자로 변경.
# 첫번째 열은 독이 있는지 없는지 2분류이기 때문에 독이 있다(1), 독이 없다(0)으로
# Label 인코더가 준비된 함수를 사용해서 분류의 수를 확인한 다음에 알아서 숫자로 분류해준다.
mush['Label'] = encoder_le.fit_transform(mush.iloc[:,0])
print(mush)

#%% mushroom의 1~22 열까지의 데이터를 모두 숫자로 변경해보자.
for i in range(1,4,1):  # 1부터 23까지(실제로 22까지) 1개씩 증가한다.
    mush['col' + str(i)] = encoder_le.fit_transform(mush.iloc[:,i])
    
print(mush)

#%% RF 모델을 위한 데이터 준비가 완료.
X = mush.loc[: , "col1":"col3"]
y = mush['Label']

print(X.shape, y.shape)  # shape은 크기를 확인하는 것.

#%% 데이터 분리
# train_test_split은 학습과 테스트데이터 셋을 기본 옵션(0.75:0.25)로 나눔.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=0)

print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

#%% RF 모델 만들기
model = RandomForestClassifier() # 모델을 생성
model.fit(X_train, y_train) # 모델을 훈련

#%% 테스트용 데이터로 예측을 해보자.
predict = model.predict(X_test)

print(len(predict))
print(predict)

# 2031개의 독인지 식용인지 예측을 했다.

#%% 예측값(predict)이 얼마나 잘 예측을 했나? 실제값(y_test)과 비교해보자.
import numpy as np

print(predict == y_test.values)
# 맞으면 True, 틀리면 False

# 갯수를 확인해보자! SUM을 하면된다.
print(np.sum(predict == y_test.values))
print((np.sum(predict == y_test.values)) / len(predict) * 100)

# 예측이 100% ?!!
# 랜덤포레스트가 일반적으로 성능이 좋더라.

#%% (실습 3-1) 학습과 테스트 데이터 셋을 50:50 으로 해보자!
import pandas as pd # 데이터 불러오기, 처리
from sklearn.ensemble import RandomForestClassifier # 랜덤포레스트 메서드
from sklearn import metrics # 학습데이터 셋을 평가하는 지표
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np

mush1 = pd.read_csv("mushroom.csv", header=None) # 제목이 없으면 header=None으로 설정.
# print(mush1)

encoder_le = preprocessing.LabelEncoder()

mush1['Label'] = encoder_le.fit_transform(mush1.iloc[:,0])
# print(mush1)

for i in range(1,23,1):  # 1부터 23까지(실제로 22까지) 1개씩 증가한다.
    mush1['col' + str(i)] = encoder_le.fit_transform(mush1.iloc[:,i])  
# print(mush1)

X1 = mush1.loc[: , "col1":"col22"]
y1 = mush1['Label']
# print(X1.shape, y1.shape)

X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.5, random_state=0)
# print(X1_train.shape, y1_train.shape)
# print(X1_test.shape, y1_test.shape)

model1 = RandomForestClassifier() # 모델을 생성
model1.fit(X1_train, y1_train)

predict1 = model1.predict(X1_test)
# print(len(predict1))
# print(predict1)
# print(predict1 == y1_test.values)
# print(np.sum(predict1 == y1_test.values))
print((np.sum(predict1 == y1_test.values)) / len(predict1) * 100)


#%% 실습(3-2) 데이터를 나눌 때, 컬럼을 1-10번까지만 써보고 결과를 확인해보자.

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np

mush2 = pd.read_csv("mushroom.csv", header=None)

encoder_le = preprocessing.LabelEncoder()

mush2['Label'] = encoder_le.fit_transform(mush2.iloc[:,0])

for i in range(1,11,1):
    mush2['col' + str(i)] = encoder_le.fit_transform(mush2.iloc[:,i])  

X2 = mush2.loc[: , "col1":"col10"]
y2 = mush2['Label']

X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.5, random_state=0)

model2 = RandomForestClassifier()
model2.fit(X2_train, y2_train)

predict2 = model2.predict(X2_test)

print((np.sum(predict2 == y2_test.values)) / len(predict2) * 100)

# 99.9015263417036

#%% 실습(3-3) 컬럼을 1-3번까지만, test_size=0.7

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import numpy as np

mush3 = pd.read_csv("mushroom.csv", header=None)

encoder_le = preprocessing.LabelEncoder()

mush3['Label'] = encoder_le.fit_transform(mush3.iloc[:,0])

for i in range(1,4,1):
    mush3['col' + str(i)] = encoder_le.fit_transform(mush3.iloc[:,i])  

X3 = mush3.loc[: , "col1":"col3"]
y3 = mush3['Label']

X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.7, random_state=0)

model3 = RandomForestClassifier()
model3.fit(X3_train, y3_train)

predict3 = model3.predict(X3_test)

print((np.sum(predict3 == y3_test.values)) / len(predict3) * 100)

# 69.96659046949182





