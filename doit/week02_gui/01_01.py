# 모듈 불러오기
from tkinter import *

c_height = 200
c_width = 300
c_colour = "black"

# Tk()는 하나의 화면이 생성(윈도우)된다. (제일 위의 윈도우)
window = Tk()
window.title("MyCanvas")

# Canvas 클래스
c = Canvas(bg=c_colour, height=c_height, width=c_width)
c.pack()

# pack() 텍스트를 표시할 만큼 레이블 위젯의 크기를 축소해라.
# label = label(window, text = "Hello World!")
# label.pack()

window.mainloop()