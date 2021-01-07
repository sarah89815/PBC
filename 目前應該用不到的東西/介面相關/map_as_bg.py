# coding: utf-8

# 引入套件
from PIL import ImageTk,Image
from tkinter import CENTER, NW, TOP
import tkinter as tk

# 建立視窗
window = tk.Tk()

# 基本元素
window.title('吃台大小幫手')
# 加號的部分是指定視窗打開時在螢幕的x,y
window.geometry("1300x700+14+7")

# 不給使用者調整大小
window.resizable(False, False)

# 背景放圖片
canvas = tk.Canvas(window, width=1300, height=700)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\JasonChen\\Desktop\\github\\self_only\\new_imagefolder\\map.png"))
# 以下是讓image好好對齊的樣子
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()
# 天尹會把修改過尺寸的地圖png檔再上傳，也就是1300x700，因為我的電腦只能顯示這麼大

window.mainloop()