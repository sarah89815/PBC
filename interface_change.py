# coding: utf-8

# 引入套件
from PIL import ImageTk,Image
from tkinter import CENTER, NW, TOP
import tkinter as tk

# 建立視窗
window = tk.Tk()

# 基本視窗元素
window.title('吃台大小幫手')
window.geometry("414x700")
window.configure(background="white")
# 不給使用者動大小
window.resizable(False, False)

# icon 待補

#"想吃甚麼"介面開始!
# 在圖形介面上設置標籤
banner = tk.Label(window, text='吃台大小幫手', bg='lightgrey' ,font=('Helvetica Neue','15'), fg = 'black')
banner.place(x=0, y=0,width=414, height=60)

# 建立你要吃什麼那個圖
firstquestion = tk.Label(window, text='你今天想吃什麼呢？', bg='lightgrey' ,font=('Helvetica Neue','15'), fg = 'black')
firstquestion.place(x=30, y=498.61,width=198, height=50)
price_b = tk.Button(text='價錢', font=('Helvetica Neue', 18), fg="black") 
price_b.place(x=126, y=573,width=83, height=41)
price_b.config(bg="orangered", fg="white")
category_b = tk.Button(window,bg='orangered',text='種類', font=('Helvetica Neue', 18))
category_b.place(x=216, y=573,width=83, height=41)
category_b.config(bg="orangered", fg="white")
value_b = tk.Button(window,bg='orangered',text='評價', font=('Helvetica Neue', 18))
value_b.place(x=306, y=573,width=83, height=41)
value_b.config(bg="orangered", fg="white")
muti_b = tk.Button(window,bg='orangered',text='複選', font=('Helvetica Neue', 18))      
muti_b.place(x=306, y=625,width=83, height=41)
muti_b.config(bg="orangered", fg="white")
country_b = tk.Button(window,bg='orangered',text='國家', font=('Helvetica Neue', 18))
country_b.place(x=216, y=625,width=83, height=41)
country_b.config(bg="orangered", fg="white")
region_b = tk.Button(window,bg='orangered',text='地區', font=('Helvetica Neue', 18))
region_b.place(x=126, y=625,width=83, height=41)
region_b.config(bg="orangered", fg="white")

'''重要！在之後的介面出現，但因為是函數(local)，所以要先放在global說有這個東西存在(不只在local)，
還沒"place"所以還不會出現。在後面有心寫到的都要補在這裡！'''
firstquestion_c = tk.Label(window, text='你今天想吃什麼呢？', bg='lightgrey' ,font=('Helvetica Neue','15'), fg = 'black')
# 為了讓使用者不再重複點種類或國家那些的，變成labal
price_b_c = tk.Label(window, text='價錢', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
category_b_c = tk.Label(window, text='種類', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
muti_b_c = tk.Label(window, text='複選', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
value_b_c = tk.Label(window, text='評價', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
country_b_c = tk.Label(window, text='國家', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
region_b_c = tk.Label(window, text='地區', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
secondquestion = tk.Label(window, text='你會想要甚麼種類呢？', bg='lightgrey' ,font=('Helvetica Neue','15'), fg = 'black')
category_chose = tk.Label(window, text='種類', bg='lightgrey' ,font=('Helvetica Neue','15'), fg='black')
category_menu_b= tk.Button(window, bg='orangered', fg="white", text='種類選單', font=('Helvetica Neue', 18))

# 按下"種類選單"後消除介面上所有對話框
def clear2_type():
    firstquestion_c.destroy()
    secondquestion.destroy()
    price_b_c.destroy()
    category_b_c.destroy()
    value_b_c.destroy()
    muti_b_c.destroy()      
    country_b_c.destroy()
    region_b_c.destroy()
    category_chose.destroy()
    category_menu_b.destroy()

#選"種類"後新增的對話框
def create_category_type():
    category_chose.place(x=306, y=523,width=80, height=40)
    category_menu_b.place(x=214, y=632,width=175, height=40)
    secondquestion.place(x=21, y=565,width=203, height=50)
    category_menu_b.config(command=clear2_type)
    
    # 選"種類"之後原對話上移(但其實是重新建造新對話框)
    firstquestion_c.place(x=30, y=359,width=198, height=50)
    price_b_c.place(x=126, y=416,width=80, height=40)
    category_b_c.place(x=216, y=416,width=80, height=40)
    value_b_c.place(x=306, y=416,width=80, height=40)     
    muti_b_c.place(x=306, y=470,width=80, height=40)
    country_b_c.place(x=216, y=470,width=80, height=40)
    region_b_c.place(x=126, y=470,width=80, height=40)

# 選"種類"後原來的按鈕不要
def clear1_type():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_category_type()
# 選"國家"後原來的按鈕不要

# 選擇"種類"後要執行的函數
category_b.config(command=clear1_type)
# 選擇"國家"後要執行的函數
# country_b.config(command=clear1_coun)














window.mainloop()