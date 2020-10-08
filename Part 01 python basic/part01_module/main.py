# _*_ coding: utf-8 _*_

"""
# seaborn 을 불러와서 약자로 sns라고 쓰겠다.
import seaborn as sns

# load_dataset 함수는 온라인 저장소에 있는 예시 데이터셋을 불러옴.
data = sns.load_dataset("tips")
print(data)
"""

"""
#%% 주피터 노트북에서와 같은 cell 형태를 만들겠다.
import mod_a

#%% 현재 위치에서 10만큼 이동
loc = 0
p_loc = mod_a.forward(loc,10)
print(p_loc)

#%% 현재 위치에서 4만큼 뒤로
p_loc = (mod_a.backward(loc,4))
print("현재 위치는: ", p_loc)
"""

#%% 다른 방법으로 불러와 보기
from mod_a import forward, backward

p_loc = 0
p_loc = forward(p_loc, 5) # 앞으로 5만큼 이동
p_loc = backward(p_loc, 4) # 앞으로 4만큼 이동

# print("현재 위치는: ", p_loc)
#%% 2-2 실행해 보기 (mod_b.py)를 불러오기
## 현재위치 추가 present_loc(loc)
## (추가) 좌, 우 몇도 변경하겠나?

p_loc = forward(0, 10)
p_loc = backward(p_loc, 3)
# print("현재 위치는: ",p_loc)