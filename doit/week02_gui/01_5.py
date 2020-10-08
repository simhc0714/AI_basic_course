from tkinter import *
import pandas as pd

global dat

dat = pd.read_excel("NPP_dict.xlsx")

# 키
def click():
    word = entry.get()
    print(word)
    
    ##
    output1.delete(0.0, END) # 삭제
    output2.delete(0.0, END) # 삭제
    
    try:
        def_word_eng = dat.loc[dat['한글용어']==word, '영문용어'].values[0]
        def_word_mean = dat.loc[dat['한글용어']==word, '용어설명'].values[0]
    except:
        def_word_eng = "단어의 뜻을 찾을 수 없습니다."
        def_word_mean = "단어의 뜻을 찾을 수 없습니다."
    
    # def_word = dict_all[word] # 딕셔너리의 키값을 이용해서 값을 가져온다.
    output1.insert(END, def_word_eng) # 추가
    output2.insert(END, def_word_mean) # 추가
    
# 메인 :
w = Tk()
w.title("원자력 용어 사전")

# 설명 레이블
label = Label(w, text="원하는 단어를 입력 후, 엔터키를 눌러주세요")
label.grid(row=0, column=0, sticky=W)

# 입력 상자(텍스트 입력) - Entry
entry = Entry(w, width=30, bg="light blue")
entry.grid(row=1, column=0, sticky=W)

# '단어 뜻 확인' 버튼 추가
btn = Button(w, text="Search", width=5, command=click)
btn.grid(row=2, column=0, sticky=W)

# 설명1(뜻 보여주는 상자에 대한) 레이블
label_eng = Label(w, text="English word")
label_eng.grid(row=3, column=0, sticky=W)

# 문단 레이블
# label_para = Label(w, text="\n")
# label_para.grid(row=1, column=0, sticky=W)

# 설명2(뜻 보여주는 상자에 대한) 레이블
label_mean = Label(w, text="Meanings")
label_mean.grid(row=7, column=0, sticky=W)

# 텍스트 상자 입력
output1 = Text(w, width=30, height=1, wrap=WORD, background="light blue")
output1.grid(row=4, column=0, columnspan=2, sticky=W)

output2 = Text(w, width=60, height=9, wrap=WORD, background="light blue")
output2.grid(row=8, column=0, columnspan=2, sticky=W)

# 단어 뜻(딕셔너리)
'''
dict_all = {
    '알고리즘' : "문제를 푸는 방법",
    '비지도학습' : "머신러닝의 한 종류로서"}
'''
w.mainloop()