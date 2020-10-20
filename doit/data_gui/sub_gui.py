import tkinter as tk
from PIL import Image, ImageTk

# Main
root = tk.Tk()
root.title = ("SEOUL METRO Pop-Time Presentation")
root.geometry("640x400+100+100")
root.resizable(True, True)

# Close Fnc
def close():
    root.quit()
    root.destroy()


# Img View Fnc
def command_args(argument1, argument2, argument3):
    global photo
    image=[]
    tmp1 = [argument1, argument2, argument3]
    tmp2 = [argument1, argument2, argument3] + tmp1
    tmp3 = [argument1, argument2, argument3] + tmp2
    
    if tmp3 == [1, 1, 1]:
        image=Image.open("C:/Users/SIMHYUNCHAE/Documents/GitHub/myrepo2/doit/line1up.png")
        photo=ImageTk.PhotoImage(image)


# Menu
menubar=tk.Menu(root)

menu_1=tk.Menu(menubar, tearoff=0, selectcolor="red")
menu_1.add_checkbutton(label="평일", command=lambda: command_args(1, 0, 0))
menu_1.add_checkbutton(label="주말", command=lambda: command_args(2, 0, 0))
menu_1.add_separator()
menu_1.add_command(label="선택 초기화", command=close)
menubar.add_cascade(label="조사일자", menu=menu_1)

menu_2=tk.Menu(menubar, tearoff=0, selectcolor="red")
menu_2.add_checkbutton(label="1호선", background="#0052A4", foreground="white", command=lambda: command_args(0, 1, 0))
menu_2.add_checkbutton(label="2호선", background="#009D3E", foreground="white", command=lambda: command_args(0, 2, 0))
menu_2.add_checkbutton(label="3호선", background="#EF7C1C", foreground="white")
menu_2.add_checkbutton(label="4호선", background="#00A5DE", foreground="white")
menu_2.add_checkbutton(label="5호선", background="#996CAC", foreground="white")
menu_2.add_checkbutton(label="6호선", background="#CD7C2F", foreground="white")
menu_2.add_checkbutton(label="7호선", background="#747F00", foreground="white")
menu_2.add_checkbutton(label="8호선", background="#EA545D", foreground="white")
menubar.add_cascade(label="호선", menu=menu_2)

menu_3=tk.Menu(menubar, tearoff=0)
menu_3.add_checkbutton(label="상행선", background="#FF0000", foreground="white", command=lambda: command_args(0, 0, 1))
menu_3.add_checkbutton(label="하행선", background="#0000FF", foreground="white", command=lambda: command_args(0, 0, 2))
menubar.add_cascade(label="역방향", menu=menu_3)

root.config(menu=menubar)

# Image Options
label_imgview=tk.Label(root, image=photo)
label_imgview.pack()


root.mainloop()

print("Windows Close")
#%%
import os
os.getcwd()