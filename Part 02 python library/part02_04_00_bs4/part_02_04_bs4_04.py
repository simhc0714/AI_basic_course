# -*- coding: utf-8 -*-
""" 2020년 10월 13일 (화) Part 02_04 파이썬 라이브러리 - bs4

파이썬 웹 크롤링
(가) 네이버 주식 정보 가져오기

"""

#%% 코드 실행시간 가져오기
import timeit
start = timeit.default_timer() # 시작 시각
stop = timeit.default_timer()
print("time :", stop - start) # 현재시각 - 시작시각 = 코드실행시간

#%% (가) 네이버 주식 정보 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

#%% KOSPI, KOSDAQ 지수 불러오기
print(soup.find_all('span', id='KOSPI_now')) # KOSPI
print(soup.find_all('span', id='KOSDAQ_now')) # KOSDAQ
print(soup.find_all('span', id='KPI200_now')) # KOSPI200

print(soup.find_all('span', id='KOSPI_now')[0].text) # KOSPI
print(soup.find_all('span', id='KOSDAQ_now')[0].text) # KOSDAQ
print(soup.find_all('span', id='KPI200_now')[0].text) # KOSPI200

#%% 실습 1
'''
    * 코스피 지수
    * 거래량(천주)
    * 거래대금(백만)
    * 52주 최저 최고 정보 가지고 오기.
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

print(soup.find('title'))
#%%
# 코스피 지수
index = soup.find_all('em', id='now_value')[0].text
print("Today's KOSPI :", index)
# 거래량 및 거래대금 가져오기
# 거래량 : td, id: quant
deal = soup.find_all('td', id='quant')[0].text
print("Today's KOSPI :", deal)

# 거래대금 : td, id: amount
deal_money = soup.find_all('td', id='amount')[0].text
print("Today's Dealling amount :", deal_money)

print("execute time :", stop - start)

#%%
kpi_index = soup.find_all('td')
# print(kpi_index)

# 장중 최고
# print("Today's high :", soup.find_all('td')[2].text)
print("Today's high :", kpi_index[2].text)

# 장중 최저
# print("Today's low :", soup.find_all('td')[3].text)
print("Today's low :", kpi_index[3].text)

# 52주 최고
# print("52 weeks' high :", soup.find_all('td')[4].text)
print("52 weeks' high :", kpi_index[4].text)

#52주 최저
# print("52 weeks' low :", soup.find_all('td')[5].text)
print("52 weeks' low :", kpi_index[5].text)

print("execute time :", stop - start)
#%% 실습 2
'''네이버 금융. 현재금액 : 자릿 수 별로 따로 떨어져서 표현돼.
안보이는 태그 확인하고 불러오기

<span class="blind">63,800</span>

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url2 = "https://finance.naver.com/item/main.nhn?code=000100"
page2 = urlopen(url2)
soup2 = BeautifulSoup(page2, 'html.parser')

print(soup2.find('title'))

# price_now = soup2.find_all('span', class_='blind'))
level_1 = soup2.find('p', class_='no_today')
level_2 = level_1.find('span', class_='blind').text
print(level_2)

dat = soup2.find('p', class_='no_today').find('span', class_='blind').text
print(dat)