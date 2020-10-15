# -*- coding: utf-8 -*-
""" 2020년 10월 13일 (화) Part 02_04 파이썬 라이브러리 - bs4

파이썬 웹 크롤링
(다) 네이버 영화 정보 가져오기

"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
#%%
url1 = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"

page = urlopen(url1)
soup = BeautifulSoup(page, "html.parser")

comment_all = soup.find_all('td', class_='title')
comment_all

#%%
url1 = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"

page = urlopen(url1)
soup = BeautifulSoup(page, "html.parser")

comment_all = soup.find_all('td', class_='title')
print( comment_all )

#%% 여러개의 댓글 가져오기
cnt = 0 
comments = []
for comment in comment_all:
    temp = list(comment.children)
    result = temp[6].strip()
    # print(result)
    comments.append(result)
    
print(comments)

#%% 1-7 페이지
comments = []
cnt = 0

basic_url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=171725&target=after&page=1"

for i in range(1,8):
    url = basic_url + str(i)
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    
    comment_all = soup.find_all('td', class_='title')
    
    for comment in comment_all:
        temp = list(comment.children)
        result = temp[6].strip()
    # print(result)
    comments.append(result)
    
print(len(comments))
print(comments)
