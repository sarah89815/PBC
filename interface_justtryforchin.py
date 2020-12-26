# coding: utf-8

# 引入套件
from PIL import ImageTk,Image
from tkinter import CENTER, NW, TOP
import tkinter as tk

# 建立視窗
window = tk.Tk()

# 基本元素
window.title('吃台大小幫手')
window.geometry("414x700")

# 不給使用者動大小
window.resizable(False, False)

# icon 待補

# 背景放圖片
canvas = tk.Canvas(window, width=414, height=700)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\JasonChen\\Desktop\\github\\self_only\\new_imagefolder\\map.png"))
# 以下是讓image好好對齊的樣子
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

# function是從按鈕倒推回來
def clear2():
	print('haha')

def create1():
	btn_d = tk.Button()
	btn_d.place(x=280, y=590, anchor=CENTER, width=40, height=24)
	btn_d.config(bg="black")
	btn_d.config(command=clear2)
	
# 開始用按鈕
def clear1():
	btn_type.destroy()
	btn_c.destroy()
	create1()


btn_type = tk.Button()
btn_type.place(x=207, y=350, anchor=CENTER, width=40, height=24)
btn_type.config(bg="skyblue")
btn_c = tk.Button()
btn_c.place(x=280, y=650, anchor=CENTER, width=40, height=24)
btn_c.config(bg="skyblue")
btn_type.config(command=clear1)

# 放圖片到button
image1 = ImageTk.PhotoImage(Image.open("C:\\Users\\JasonChen\\Desktop\\github\\self_only\\new_imagefolder\\try1.png"))
btn_c.config(image=image1)

