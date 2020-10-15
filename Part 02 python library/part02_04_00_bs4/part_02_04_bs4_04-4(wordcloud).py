# -*- coding: utf-8 -*-
from wordcloud import WordCloud, STOPWORDS

import numpy as np
from PIL import Image

import os
print(os.getcwd())

#%%
f = open("스파이더맨리뷰.csv", encoding='utf-8')

text = f.read()
f.close()

#%%
from matplotlib import rc
rc('font', family='NanumGothic')

#%%
%matplotlib inline
from wordcloud import WordCloud
wcloud = WordCloud('.data/D2Coding.ttf', max_words=1000, relative_scaling=)

import matplotlib.pyplot as plt
plt.figure(figsize=(12,12))
plit.imshow(wcloud, interpolation='bilinear')
plt.axis("off")
lit.show()