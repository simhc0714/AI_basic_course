# -*- coding: utf-8 -*-
""" 020년 10월 13일 (화) Part 02_04 파이썬 라이브러리 - bs4

파이썬 웹 크롤링
(나) 여러개의 웹 정보 가져오기

    * 여러개의 웹 정보를 불러오려면 공통된 특징을 알아야한다.
    * NAVER: "https://finance.naver.com/item/main.nhn?code=035420"
    * 삼성전자: "https://finance.naver.com/item/main.nhn?code=005930"
"""

#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

my_stock = ['삼성전자', '카카오', '유한양행', 'NAVER', '셀트리온', '현대차']
my_stock_code = ['005930','035720', '000100', '035420', '068270', '005380']

base_url = 'https://finance.naver.com/item/main.nhn?code='

#%% for 구문으로 코드 넣어서 가격 가져오기.
# init
com = [] # 회사명
code_p = []
price_c = [] # 가격

cnt = 0

for code in my_stock_code:
    # cnt = 0
    all_url = base_url + code
    page = urlopen(all_url)
    soup = BeautifulSoup(page, 'lxml')
    
    ## 현재가
    tmp = soup.find('p', class_='no_today')
    price = tmp.find('span', class_='blind').text
    
    com.append(my_stock[cnt])
    code_p.append(my_stock_code[cnt])
    price_c.append(price)
    
    cnt += 1 # cnt = cnt + 1
    
print(com)
print(price_c)
print(code_p)

#%%
import pandas as pd

a = [1,2,3,4]
dict = {"회사" : com,
        "코드" : code_p,
        "현재가" : price_c}

dat = pd.DataFrame(dict)
print(dat)

# 엑셀로 만들고 싶다.
dat.to_excel("stock.xlsx", index=False)

# csv a, b, c
dat.to_csv("stock.csv", index=False, encoding='ms949')
