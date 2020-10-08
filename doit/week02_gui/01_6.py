import pandas as pd

dat = pd.read_excel("dict01.xlsx")
# print(dat)

# print(dat.info()) # 파일의 정보를 보여줍니다.

# print(dat.describe()) # 파일의 요약 정보를 보여줍니다.

# print(dat['']) 다음 레이블의 열만 불러옵니다.
# print(dat['단어'])
# print(dat['뜻'])


dat(['알고리즘']=="word", '뜻')