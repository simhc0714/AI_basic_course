# -*- coding: utf-8 -*-
#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"
page = urlopen(url)
 
soup = BeautifulSoup(page, 'lxml')
#%% soup.find() 메서드는 첫번째 태그를 가져온다.
'''위의 셀이 잘 실행되었는지를 확인하기위하여 웹사이트의 title을 가져와 보자'''
key_title = soup.find('title')
title_text = key_title.text
print(title_text)
      
#%% soup.find_all() 메서드는 해당하는 모든 태그를 가져온다.
link_all = soup.find_all('a')
print(link_all)
 
for i in link_all:
     print(i)

#%% 네이버 금융 정보 가져오기


#%% Exercise 3-3 인기 검색 종목 10개

# tag : ul
# class : lst_pop
li_all = soup.find("ul", class_="lst_pop")

# print(li_all)

a_all = li_all.find_all("a")
li_span = li_all.find_all("span")

for i in a_all:
    print(i.text)
    
cnt = 0
for i in li_span:
    if cnt%2==0:
       print(i.text) 
   cnt = cnt + 1
   

