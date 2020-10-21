import tkinter as tk
from PIL import Image, ImageTk

window=tk.Tk()
window.title("SEOUL METRO Pop-Time Viewer")
window.geometry("1750x800+100+100")
window.resizable(True, True)

#--initialize--
# image=[]

def command_args(num):
    global photo
    # image=[]
    if num == 1:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line1up.png")
    elif num == 2:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line2up.png")
    elif num == 3:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line3up.png")
    elif num == 4:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line4up.png")
    elif num == 5:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line5up.png")
    elif num == 6:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line6up.png")
    elif num == 7:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line7up.png")
    elif num == 8:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line8up.png")
    elif num == 0:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/init.png")
        # Image.close()
        
    photo=ImageTk.PhotoImage(image)
    
    # canvas = tk.Canvas(height=700, width=1750)
    # canvas.image = photo
    # canvas.create_image(frame3, image=photo)
    # canvas.pack(expand=True, fill="both")
    # Image Options
    label_imgview=tk.Label(frame3, image=photo)
    label_imgview.pack(expand=True, fill="both")

    

#--Gen Frame--
frame1=tk.Frame(window, relief="solid", bd=1)
frame1.pack(side="top", fill="x")

frame_b=tk.Frame(window, height=5, relief="flat")
frame_b.pack(side="top", fill="x")

frame2=tk.Frame(window, relief="solid", bd=1)
frame2.pack(side="top", fill="x")

frame3=tk.Frame(window, relief="solid", bd=1)
frame3.pack(expand=True, fill="both")


#--Gen Button on Frame1--
# 주말 기능 사용할 수 없음
btn_wkd=tk.Button(frame1, text="평일", state='disabled', background="#00FF00", width=15)
btn_wke=tk.Button(frame1, text="주말", state='disabled', background="#00FF00", width=15)
btn_wkd.pack(side="left", fill="y")
btn_wke.pack(side="left", fill="y")

# 하행선 기능 사용할 수 없음
b13=tk.Button(frame1, text="하행선", state='disabled', background="#00FF00", width=15)
b14=tk.Button(frame1, text="상행선", state='disabled', background="#00FF00", width=15)
b13.pack(side="right", fill="y")
b14.pack(side="right", fill="y")

label1=tk.Label(frame1, text="Team 2", font=("Arial", 20))
label_ntc=tk.Label(frame_b, text="알림: 현재 오류로 인해 평일-주말, 상-하행선 기능을 사용할수 없음.", foreground="red")
label1.pack(side="top", anchor="center", fill="x")
label_ntc.pack(side="top", anchor="center", fill="x")


#--Gen Button on Frame2--
b21=tk.Button(frame2, text="1호선", background="#0052A4", width=20, command=lambda: command_args(1))
b21.pack(side="left", fill="y")
b22=tk.Button(frame2, text="2호선", background="#009D3E", width=20, command=lambda: command_args(2))
b22.pack(side="left", fill="y")
b23=tk.Button(frame2, text="3호선", background="#EF7C1C", width=20, command=lambda: command_args(3))
b23.pack(side="left", fill="y")
b24=tk.Button(frame2, text="4호선", background="#00A5DE", width=20, command=lambda: command_args(4))
b24.pack(side="left", fill="y")

btn_init=tk.Button(frame2, text="초기화", activebackground="#00FF00", width=20, command=lambda: command_args(0))
btn_init.pack(side="left", fill="y")

b25=tk.Button(frame2, text="9호선", background="#BDB092", width=20, state='disabled')
b25.pack(side="right", fill="y")
b26=tk.Button(frame2, text="8호선", background="#996CAC", width=20, command=lambda: command_args(5))
b26.pack(side="right", fill="y")
b27=tk.Button(frame2, text="7호선", background="#CD7C2F", width=20, command=lambda: command_args(6))
b27.pack(side="right", fill="y")
b28=tk.Button(frame2, text="6호선", background="#747F00", width=20, command=lambda: command_args(7))
b28.pack(side="right", fill="y")
b29=tk.Button(frame2, text="5호선", background="#EA545D", width=20, command=lambda: command_args(8))
b29.pack(side="right", fill="y")

label2=tk.Label(frame2, text="심현채, 최종운, 장상희", font=("Arial", 14))
label2.pack(side="top", anchor="center", fill="x")


window.mainloop()