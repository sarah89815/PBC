# coding: utf-8

# 引入套件
from PIL import ImageTk,Image
from tkinter import CENTER, NW, TOP
import tkinter as tk
import csv
# 地圖標點用的套件
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.offsetbox import AnnotationBbox, TextArea
import numpy as np

# 建立傳入演算法的清單
keyword = list()
upperbound = str()
lowerbound = str()

# 建立視窗
window = tk.Tk()

# 基本視窗元素
window.title('吃台大小幫手')
window.geometry("414x700")
window.configure(background="white")
# 不給使用者動大小
window.resizable(False, False)

# icon 待補
#背景圖
canvas = tk.Canvas(window, width=414,height=700,bg = 'white')
imgpath = r'C:\\Users\\JasonChen\\Desktop\\github\\self_only\\back.png'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas.create_image(212, 350,image=photo)
canvas.pack()
# "想吃甚麼"介面開始!
# 在圖形介面上設置標籤
banner = tk.Label(window, text='吃台大小幫手', bg='coral' ,font=('Helvetica Neue','30'), fg = 'white')
banner.place(x=0, y=0,width=414, height=60)

# 建立你要吃什麼那個圖
firstquestion = tk.Label(window, text='你今天想吃什麼呢？', bg='cornsilk', borderwidth = 1,font=('Helvetica Neue','18'), fg = 'saddlebrown')
firstquestion.place(x=21, y=498.61,width=211, height=50)
price_b = tk.Button(text='價錢', font=('Helvetica Neue', 18), bg="coral") 
price_b.place(x=126, y=573,width=83, height=41)
price_b.config(bg="coral", fg="saddlebrown")
category_b = tk.Button(window,text='種類', font=('Helvetica Neue', 18))
category_b.place(x=216, y=573,width=83, height=41)
category_b.config(bg="coral", fg="saddlebrown")
value_b = tk.Button(window,text='評價', font=('Helvetica Neue', 18))
value_b.place(x=306, y=573,width=83, height=41)
value_b.config(bg="coral", fg="saddlebrown")
muti_b = tk.Button(window,text='複選', font=('Helvetica Neue', 18))      
muti_b.place(x=306, y=625,width=83, height=41)
muti_b.config(bg="coral", fg="saddlebrown")
country_b = tk.Button(window,text='國家', font=('Helvetica Neue', 18))
country_b.place(x=216, y=625,width=83, height=41)
country_b.config(bg="coral", fg="saddlebrown")
region_b = tk.Button(window,text='地區', font=('Helvetica Neue', 18))
region_b.place(x=126, y=625,width=83, height=41)
region_b.config(bg="coral", fg="saddlebrown")

'''重要！在之後的介面出現，但因為是函數(local)，所以要先放在global說有這個東西存在(不只在local)，
還沒"place"所以還不會出現。在後面有新寫到的都要補在這裡！'''
firstquestion_c = tk.Label(window, text='你今天想吃什麼呢？', bg='cornsilk' ,font=('Helvetica Neue','15'), fg = 'saddlebrown')
# 為了讓使用者不再重複點種類或國家那些的，變成label
price_b_c = tk.Label(window, text='價錢', font=('Helvetica Neue', 15), bg='coral', fg='white')
category_b_c = tk.Label(window, text='種類', font=('Helvetica Neue', 15), bg='coral', fg='white')
muti_b_c = tk.Label(window, text='複選', font=('Helvetica Neue', 15), bg='coral', fg='white')
value_b_c = tk.Label(window, text='評價', font=('Helvetica Neue', 15), bg='coral', fg='white')
country_b_c = tk.Label(window, text='國家', font=('Helvetica Neue', 15), bg='coral', fg='white')
region_b_c = tk.Label(window, text='地區', font=('Helvetica Neue', 15), bg='coral', fg='white')
# 最後一個對話框
finish = tk.Label(window, text='我幫你找到符合條件的餐廳了！\n \n可以移動游標到圖釘了解餐廳資訊喔', font=('Helvetica Neue', 12), bg='cornsilk', fg='saddlebrown')
go = tk.Button(window, bg='coral', fg="white", text="Let's go!", font=('Helvetica Neue', 13))
# type線的部分
secondquestion_type = tk.Label(window, text='你會想要甚麼種類呢？', bg='cornsilk',font=('Helvetica Neue',15), fg = 'saddlebrown')
category_chose = tk.Label(window, text='種類', bg='gold' ,font=('Helvetica Neue', 15), fg='white')
category_menu_b= tk.Button(window, bg='coral', fg="saddlebrown", text='種類選單', font=('Helvetica Neue', 18))
type_label = tk.Label(window, text='種類', bg='white', font=('Helvetica Neue',19), fg='grey')
multichoice_label = tk.Label(window, text='可複選', bg='white', font=('Helvetica Neue',10), fg='lightgrey')
type_b1 = tk.Button(window, text='義大利麵', bg='cornsilk', fg="saddlebrown", font=('Helvetica Neue', 13))
type_b2 = tk.Button(window, text='咖哩飯',bg='cornsilk', fg="saddlebrown", font=('Helvetica Neue', 13))
type_b3 = tk.Button(window, text='早午飯',bg='cornsilk', fg="saddlebrown", font=('Helvetica Neue', 13))
type_b4 = tk.Button(window, text='河粉',bg='cornsilk', fg="saddlebrown", font=('Helvetica Neue', 13))
type_b5 = tk.Button(window, text='飯類',bg='cornsilk', fg="saddlebrown", font=('Helvetica Neue', 13))
type_b6 = tk.Button(window, text='麵類',bg='cornsilk', fg="saddlebrown", font=('Helvetica Neue', 13))
type_b7 = tk.Button(window, text='火鍋',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b8 = tk.Button(window, text='水餃',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b9 = tk.Button(window, text='披薩',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b10 = tk.Button(window, text='燉飯',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b11 = tk.Button(window, text='排餐',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b12 = tk.Button(window, text='早餐',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b13 = tk.Button(window, text='素食',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b14 = tk.Button(window, text='漢堡',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b15 = tk.Button(window, text='沙拉',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b16 = tk.Button(window, text='飯糰',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b17 = tk.Button(window, text='炸物',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b18 = tk.Button(window, text='粥',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b19 = tk.Button(window, text='吐司麵包',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b20 = tk.Button(window, text='烤肉',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b21 = tk.Button(window, text='便當',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b22 = tk.Button(window, text='蛋包飯',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b23 = tk.Button(window, text='關東煮',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b24 = tk.Button(window, text='滷味',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b25 = tk.Button(window, text='壽喜燒',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b26 = tk.Button(window, text='咖啡廳',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b27 = tk.Button(window, text='甜點',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b28 = tk.Button(window, text='冰品',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b29 = tk.Button(window, text='鹹食',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
type_b30 = tk.Button(window, text='確定', bg='coral', fg='white', font=('Helvetica Neue', 13))
# country線的部分
secondquestion_country = tk.Label(window, text='你會想要哪國的料理呢？', bg='cornsilk' ,font=('Helvetica Neue',15), fg = 'saddlebrown')
country_chose = tk.Label(window, text='國家', bg='gold',font=('Helvetica Neue', 15), fg='white')
country_menu_b= tk.Button(window, bg='coral', fg="white", text='異國料理種類選單', font=('Helvetica Neue', 18))
country_label = tk.Label(window, text='異國料理種類', bg='white', font=('Helvetica Neue',19), fg='grey')
multichoice_label = tk.Label(window, text='可複選', bg='white', font=('Helvetica Neue',10), fg='lightgrey')
country_b1 = tk.Button(window, text='日式壽司',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b2 = tk.Button(window, text='日式丼飯',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b3 = tk.Button(window, text='日式拉麵',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b4 = tk.Button(window, text='韓式料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b5 = tk.Button(window, text='中東料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b6 = tk.Button(window, text='印度料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b7 = tk.Button(window, text='港式料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b8 = tk.Button(window, text='越式料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b9 = tk.Button(window, text='泰式料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b10 = tk.Button(window, text='俄羅斯料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b11 = tk.Button(window, text='地中海料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b12 = tk.Button(window, text='馬來西亞料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b13 = tk.Button(window, text='雲南料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b14 = tk.Button(window, text='四川料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b15 = tk.Button(window, text='南洋料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b16 = tk.Button(window, text='以色列料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b17 = tk.Button(window, text='加拿大料理',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b18 = tk.Button(window, text='夏威夷生魚飯',bg='cornsilk', fg='saddlebrown', font=('Helvetica Neue', 13))
country_b19 = tk.Button(window, text='確定', bg='coral', fg='white', font=('Helvetica Neue', 13))
# region線的部分
secondquestion_region = tk.Label(window, text='你會想要在那裡吃呢？', bg='cornsilk' ,font=('Helvetica Neue',15), fg = 'saddlebrown')
region_chose = tk.Label(window, text='地區', bg='gold',font=('Helvetica Neue', 15), fg='white')
multichoice_label = tk.Label(window, text='可複選', bg='white', font=('Helvetica Neue',10), fg='lightgrey')
region_b1 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='溫州街', font=('Helvetica Neue', 15))
region_b2 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='後門', font=('Helvetica Neue', 15))
region_b3 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='公館', font=('Helvetica Neue', 15))
region_confirm = tk.Button(window, bg='coral', fg='white', text='確定', font=('Helvetica Neue', 12))
region_l1 = tk.Label(window, text='溫州街', bg='coral',font=('Helvetica Neue', 15), fg='white')
region_l2 = tk.Label(window, text='後門', bg='coral',font=('Helvetica Neue', 15), fg='white')
region_l3 = tk.Label(window, text='公館', bg='coral',font=('Helvetica Neue', 15), fg='white')
# price線的部分
secondquestion_price = tk.Label(window, text='你想要甚麼價位呢？', bg='cornsilk' ,font=('Helvetica Neue',15), fg = 'saddlebrown')
price_chose = tk.Label(window, text='價錢', bg='gold',font=('Helvetica Neue', 15), fg='white')
price_b1 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $100', font=('Helvetica Neue', 15))
price_b2 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $200', font=('Helvetica Neue', 15))
price_b3 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $300', font=('Helvetica Neue', 15))
price_b4 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $400', font=('Helvetica Neue', 15))
price_b5 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $500', font=('Helvetica Neue', 15))
price_b6 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $600', font=('Helvetica Neue', 15))
price_b7 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $700', font=('Helvetica Neue', 15))
price_b8 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $800', font=('Helvetica Neue', 15))
# value線的部分
secondquestion_value = tk.Label(window, text='你對評價的要求是甚麼？', bg='cornsilk' ,font=('Helvetica Neue',15), fg = 'saddlebrown')
value_chose = tk.Label(window, text='評價', bg='coral',font=('Helvetica Neue', 15), fg='white')
value_b1 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>= 1星', font=('Helvetica Neue', 15))
value_b2 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>= 2星', font=('Helvetica Neue', 15))
value_b3 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>= 3星', font=('Helvetica Neue', 15))
value_b4 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>= 4星', font=('Helvetica Neue', 15))
value_b5 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>= 5星', font=('Helvetica Neue', 15))
#multi線的部分
filter_label = tk.Label(window, text='篩選', bg='white', font=('Helvetica Neue', 18), fg='black')
type_label = tk.Label(window, text='種類',bg='white', font=('Helvetica Neue', 15), fg='black')
country_label = tk.Label(window, text='種類（以國家分）', bg='white',font=('Helvetica Neue', 15), fg='black')
region_label = tk.Label(window, text='地區', bg='white',font=('Helvetica Neue', 15), fg='black')
price_label = tk.Label(window, text='價格', bg='white',font=('Helvetica Neue', 15), fg='black')
value_label = tk.Label(window, text='評價', bg='white',font=('Helvetica Neue', 15), fg='black')
country_menu_b= tk.Button(window, bg='cornsilk', fg="saddlebrown", text='異國料理種類選單', font=('Helvetica Neue', 15))
type_menu_b= tk.Button(window, bg='cornsilk', fg="saddlebrown", text='種類選單', font=('Helvetica Neue', 15))
region_b1 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='溫州街', font=('Helvetica Neue', 15))
region_b2 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='後門', font=('Helvetica Neue', 15))
region_b3 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='公館', font=('Helvetica Neue', 15))
price_b1 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $100', font=('Helvetica Neue', 15))
price_b2 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $200', font=('Helvetica Neue', 15))
price_b3 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $300', font=('Helvetica Neue', 15))
price_b4 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $400', font=('Helvetica Neue', 15))
price_b5 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $500', font=('Helvetica Neue', 15))
price_b6 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $600', font=('Helvetica Neue', 15))
price_b7 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $700', font=('Helvetica Neue', 15))
price_b8 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='< $800', font=('Helvetica Neue', 15))
value_b1 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>=1星', font=('Helvetica Neue', 15))
value_b2 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>=2星', font=('Helvetica Neue', 15))
value_b3 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>=3星', font=('Helvetica Neue', 15))
value_b4 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>=4星', font=('Helvetica Neue', 15))
value_b5 = tk.Button(window, bg='cornsilk', fg="saddlebrown", text='>=5星', font=('Helvetica Neue', 15))
confirm_b = tk.Button(window, text='確定', bg='coral', fg='white', font=('Helvetica Neue', 13))
#multi中的種類線（要更新的地方）
type_label_1 = tk.Label(window, text='種類', bg='white', font=('Helvetica Neue',19), fg='grey')
multichoice_label_1 = tk.Label(window, text='可複選', bg='white', font=('Helvetica Neue',10), fg='lightgrey')
#multi中的國家線（要更新的地方）
country_label_1 = tk.Label(window, text='異國料理種類', bg='white', font=('Helvetica Neue',19), fg='grey')
multichoice_label_1 = tk.Label(window, text='可複選', bg='white', font=('Helvetica Neue',10), fg='lightgrey')



'''六條線都需要的函數'''
# 消除之前介面上「原始的」對話框，適用所有線!(因為最原始的對話大家都一樣)
def clear2_forall():
    firstquestion_c.destroy()
    price_b_c.destroy()
    category_b_c.destroy()
    value_b_c.destroy()
    muti_b_c.destroy()      
    country_b_c.destroy()
    region_b_c.destroy()

# 種類、國家、地區線都相同的函數!(原對話上移，但其實是重新建造新對話框)
def moveup():
    firstquestion_c.place(x=21, y=359,width=211, height=50)
    price_b_c.place(x=126, y=416,width=80, height=40)
    category_b_c.place(x=216, y=416,width=80, height=40)
    value_b_c.place(x=306, y=416,width=80, height=40)     
    muti_b_c.place(x=306, y=470,width=80, height=40)
    country_b_c.place(x=216, y=470,width=80, height=40)
    region_b_c.place(x=126, y=470,width=80, height=40)

# 按下let's go把視窗關閉跳出地圖部分
def gogo():
    window.destroy()


# 按下"確定"或是其他確認按鈕後跳出最後一個對話框+接上地圖部分
def lastmove():
    finish.place(x=35, y=290,width=345, height=91)
    go.place(x=200, y=422,width=100, height=27, anchor=CENTER)
    go.config(command=gogo)

'''種類函數區'''
# 按了某種類之後，變顏色，傳出keyword給演算法(不變成標籤，太麻煩；不給重複按，太麻煩)
def userchoice_typeb1():
    type_b1.config(bg='coral', fg='white')
    keyword.append('義大利麵')
def userchoice_typeb2():
    type_b2.config(bg='coral', fg='white')
    keyword.append('咖哩飯')
def userchoice_typeb3():
    type_b3.config(bg='coral', fg='white')
    keyword.append('早午餐')
def userchoice_typeb4():
    type_b4.config(bg='coral', fg='white')
    keyword.append('河粉')
def userchoice_typeb5():
    type_b5.config(bg='coral', fg='white')
    keyword.append('飯類')
def userchoice_typeb6():
    type_b6.config(bg='coral', fg='white')
    keyword.append('麵類')
def userchoice_typeb7():
    type_b7.config(bg='coral', fg='white')
    keyword.append('火鍋')
def userchoice_typeb8():
    type_b8.config(bg='coral', fg='white')
    keyword.append('水餃')
def userchoice_typeb9():
    type_b9.config(bg='coral', fg='white')
    keyword.append('披薩')
def userchoice_typeb10():
    type_b10.config(bg='coral', fg='white')
    keyword.append('燉飯')
def userchoice_typeb11():
    type_b11.config(bg='coral', fg='white')
    keyword.append('排餐')
def userchoice_typeb12():
    type_b12.config(bg='coral', fg='white')
    keyword.append('早餐')
def userchoice_typeb13():
    type_b13.config(bg='coral', fg='white')
    keyword.append('素食')
def userchoice_typeb14():
    type_b14.config(bg='coral', fg='white')
    keyword.append('漢堡')
def userchoice_typeb15():
    type_b15.config(bg='coral', fg='white')
    keyword.append('沙拉')
def userchoice_typeb16():
    type_b16.config(bg='coral', fg='white')
    keyword.append('飯糰')
def userchoice_typeb17():
    type_b17.config(bg='coral', fg='white')
    keyword.append('炸物')
def userchoice_typeb18():
    type_b18.config(bg='coral', fg='white')
    keyword.append('粥')
def userchoice_typeb19():
    type_b19.config(bg='coral', fg='white')
    keyword.append('吐司麵包')
def userchoice_typeb20():
    type_b20.config(bg='coral', fg='white')
    keyword.append('烤肉')
def userchoice_typeb21():
    type_b21.config(bg='coral', fg='white')
    keyword.append('便當')
def userchoice_typeb22():
    type_b22.config(bg='coral', fg='white')
    keyword.append('蛋包飯')
def userchoice_typeb23():
    type_b23.config(bg='coral', fg='white')
    keyword.append('關東煮')
def userchoice_typeb24():
    type_b24.config(bg='coral', fg='white')
    keyword.append('滷味')
def userchoice_typeb25():
    type_b25.config(bg='coral', fg='white')
    keyword.append('壽喜燒')
def userchoice_typeb26():
    type_b26.config(bg='coral', fg='white')
    keyword.append('咖啡廳')
def userchoice_typeb27():
    type_b27.config(bg='coral', fg='white')
    keyword.append('甜點')
def userchoice_typeb28():
    type_b28.config(bg='coral', fg='white')
    keyword.append('冰品')
def userchoice_typeb29():
    type_b29.config(bg='coral', fg='white')
    keyword.append('鹹食')

# 按下"確定"後把當前所有按鈕標籤清理掉+跳到最後畫面
def confirm_type():
    type_label.destroy()
    multichoice_label.destroy()
    type_b1.destroy()
    type_b2.destroy()
    type_b3.destroy()
    type_b4.destroy()
    type_b5.destroy()
    type_b6.destroy()
    type_b7.destroy()
    type_b8.destroy()
    type_b9.destroy()
    type_b10.destroy()
    type_b11.destroy()
    type_b12.destroy()
    type_b13.destroy()
    type_b14.destroy()
    type_b15.destroy()
    type_b16.destroy()
    type_b17.destroy()
    type_b18.destroy()
    type_b19.destroy()
    type_b20.destroy()
    type_b21.destroy()
    type_b22.destroy()
    type_b23.destroy()
    type_b24.destroy()
    type_b25.destroy()
    type_b26.destroy()
    type_b27.destroy()
    type_b28.destroy()
    type_b29.destroy()
    type_b30.destroy()
    lastmove()

# 按下"種類選單"後要新增的按鈕們
def create2_type():
    type_label.place(x=38, y=102,width=46, height=40)
    multichoice_label.place(x=38, y=145,width=39, height=17)
    type_b1.place(x=34, y=172,width=91, height=37)
    type_b1.config(command=userchoice_typeb1)
    type_b2.place(x=160, y=172,width=91, height=37)
    type_b2.config(command=userchoice_typeb2)
    type_b3.place(x=283, y=172,width=91, height=37)
    type_b3.config(command=userchoice_typeb3)
    type_b4.place(x=34, y=219,width=91, height=37)
    type_b4.config(command=userchoice_typeb4)
    type_b5.place(x=160, y=219,width=91, height=37)
    type_b5.config(command=userchoice_typeb5)
    type_b6.place(x=283, y=219,width=91, height=37)
    type_b6.config(command=userchoice_typeb6)
    type_b7.place(x=34, y=265,width=91, height=37)
    type_b7.config(command=userchoice_typeb7)
    type_b8.place(x=160, y=265,width=91, height=37)
    type_b8.config(command=userchoice_typeb8)
    type_b9.place(x=283, y=265,width=91, height=37)
    type_b9.config(command=userchoice_typeb9)
    type_b10.place(x=34, y=312,width=91, height=37)
    type_b10.config(command=userchoice_typeb10)
    type_b11.place(x=160, y=312,width=91, height=37)
    type_b11.config(command=userchoice_typeb11)
    type_b12.place(x=283, y=312,width=91, height=37)
    type_b12.config(command=userchoice_typeb12)
    type_b13.place(x=34, y=358, width=91, height=37)
    type_b13.config(command=userchoice_typeb13)
    type_b14.place(x=160, y=358, width=91, height=37)
    type_b14.config(command=userchoice_typeb14)
    type_b15.place(x=283, y=358, width=91, height=37)
    type_b15.config(command=userchoice_typeb15)
    type_b16.place(x=34, y=405, width=91, height=37)
    type_b16.config(command=userchoice_typeb16)
    type_b17.place(x=160, y=405, width=91, height=37)
    type_b17.config(command=userchoice_typeb17)
    type_b18.place(x=283, y=405, width=91, height=37)
    type_b18.config(command=userchoice_typeb18)
    type_b19.place(x=34, y=451, width=91, height=37)
    type_b19.config(command=userchoice_typeb19)
    type_b20.place(x=160, y=451, width=91, height=37)
    type_b20.config(command=userchoice_typeb20)
    type_b21.place(x=283, y=451, width=91, height=37)
    type_b21.config(command=userchoice_typeb21)
    type_b22.place(x=34, y=498,width=91, height=37)
    type_b22.config(command=userchoice_typeb22)
    type_b23.place(x=160, y=498,width=91, height=37)
    type_b23.config(command=userchoice_typeb23)
    type_b24.place(x=283, y=498,width=91, height=37)
    type_b24.config(command=userchoice_typeb24)
    type_b25.place(x=34, y=544,width=91, height=37)
    type_b25.config(command=userchoice_typeb25)
    type_b26.place(x=160, y=544,width=91, height=37)
    type_b26.config(command=userchoice_typeb26)
    type_b27.place(x=283, y=544,width=91, height=37)
    type_b27.config(command=userchoice_typeb27)
    type_b28.place(x=34, y=591,width=91, height=37)
    type_b28.config(command=userchoice_typeb28)
    type_b29.place(x=160, y=591, width=91, height=37)
    type_b29.config(command=userchoice_typeb29)
    type_b30.place(x=156, y=638,width=102, height=49)
    type_b30.config(command=confirm_type)

# 按下"種類選單"後消除之前介面上「新增的」對話
def clear2_type():
    secondquestion_type.destroy()
    category_chose.destroy()
    category_menu_b.destroy()

'''按下"種類選單"後
a.消除介面上「所有的」對話框
b.要新增的對話框(很多)'''
def clr2crt2_type():
    clear2_type()
    clear2_forall()
    create2_type()

#選"種類"後新增的對話框
def create_type():
    category_chose.place(x=306, y=523,width=80, height=40)
    category_menu_b.place(x=214, y=632,width=175, height=40)
    secondquestion_type.place(x=21, y=565,width=225, height=50)
    category_menu_b.config(command=clr2crt2_type)

# 選"種類"後原來的按鈕不要+上移
def clear1_type():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_type()
    moveup()

'''國家函數區'''
# 按下"國家選單"後消除之前介面上「新增的」對話
def clear2_country():
    secondquestion_country.destroy()
    country_chose.destroy()
    country_menu_b.destroy()

# 按了料理之後，變顏色，傳出keyword給演算法(不變成標籤，太麻煩；不給重複按，太麻煩)
def userchoice_countryb1():
    country_b1.config(bg='coral', fg='white')
    keyword.append('日式壽司')
def userchoice_countryb2():
    country_b2.config(bg='coral', fg='white')
    keyword.append('日式丼飯')
def userchoice_countryb3():
    country_b3.config(bg='coral', fg='white')
    keyword.append('日式拉麵')
def userchoice_countryb4():
    country_b4.config(bg='coral', fg='white')
    keyword.append('韓式料理')
def userchoice_countryb5():
    country_b5.config(bg='coral', fg='white')
    keyword.append('中東料理')
def userchoice_countryb6():
    country_b6.config(bg='coral', fg='white')
    keyword.append('印度料理')
def userchoice_countryb7():
    country_b7.config(bg='coral', fg='white')
    keyword.append('港式料理')
def userchoice_countryb8():
    country_b8.config(bg='coral', fg='white')
    keyword.append('越式料理')
def userchoice_countryb9():
    country_b9.config(bg='coral', fg='white')
    keyword.append('泰式料理')
def userchoice_countryb10():
    country_b10.config(bg='coral', fg='white')
    keyword.append('俄羅斯料理')
def userchoice_countryb11():
    country_b11.config(bg='coral', fg='white')
    keyword.append('地中海料理')
def userchoice_countryb12():
    country_b12.config(bg='coral', fg='white')
    keyword.append('馬來西亞料理')
def userchoice_countryb13():
    country_b13.config(bg='coral', fg='white')
    keyword.append('雲南料理')
def userchoice_countryb14():
    country_b14.config(bg='coral', fg='white')
    keyword.append('四川料理')
def userchoice_countryb15():
    country_b15.config(bg='coral', fg='white')
    keyword.append('南洋料理')
def userchoice_countryb16():
    country_b16.config(bg='coral', fg='white')
    keyword.append('以色列料理')
def userchoice_countryb17():
    country_b17.config(bg='coral', fg='white')
    keyword.append('加拿大料理')
def userchoice_countryb18():
    country_b18.config(bg='coral', fg='white')
    keyword.append('夏威夷生魚飯')

# 按下"確定"後把當前所有按鈕標籤清理掉+跳到最後畫面
def confirm_country():
    country_label.destroy()
    multichoice_label.destroy()
    country_b1.destroy()
    country_b2.destroy()
    country_b3.destroy()
    country_b4.destroy()
    country_b5.destroy()
    country_b6.destroy()
    country_b7.destroy()
    country_b8.destroy()
    country_b9.destroy()
    country_b10.destroy()
    country_b11.destroy()
    country_b12.destroy()
    country_b13.destroy()
    country_b14.destroy()
    country_b15.destroy()
    country_b16.destroy()
    country_b17.destroy()
    country_b18.destroy()
    country_b19.destroy()
    lastmove()

# 按下"國家選單"後要新增的按鈕們
def create2_country():
    country_label.place(x=38, y=114,width=160, height=40)
    multichoice_label.place(x=38, y=171,width=39, height=17)
    country_b1.place(x=26, y=212,width=113, height=51)
    country_b1.config(command=userchoice_countryb1)
    country_b2.place(x=151, y=212,width=113, height=51)
    country_b2.config(command=userchoice_countryb2)
    country_b3.place(x=277, y=212,width=113, height=51)
    country_b3.config(command=userchoice_countryb3)
    country_b4.place(x=26, y=283,width=113, height=51)
    country_b4.config(command=userchoice_countryb4)
    country_b5.place(x=151, y=283,width=113, height=51)
    country_b5.config(command=userchoice_countryb5)
    country_b6.place(x=277, y=283,width=113, height=51)
    country_b6.config(command=userchoice_countryb6)
    country_b7.place(x=26, y=354,width=113, height=51)
    country_b7.config(command=userchoice_countryb7)
    country_b8.place(x=151, y=354,width=113, height=51)
    country_b8.config(command=userchoice_countryb8)
    country_b9.place(x=277, y=354,width=113, height=51)
    country_b9.config(command=userchoice_countryb9)
    country_b10.place(x=26, y=425,width=113, height=51)
    country_b10.config(command=userchoice_countryb10)
    country_b11.place(x=151, y=425,width=113, height=51)
    country_b11.config(command=userchoice_countryb11)
    country_b12.place(x=277, y=425,width=113, height=51)
    country_b12.config(command=userchoice_countryb12)
    country_b13.place(x=26, y=496,width=113, height=51)
    country_b13.config(command=userchoice_countryb13)
    country_b14.place(x=151, y=496,width=113, height=51)
    country_b14.config(command=userchoice_countryb14)
    country_b15.place(x=277, y=496,width=113, height=51)
    country_b15.config(command=userchoice_countryb15)
    country_b16.place(x=26, y=567,width=113, height=51)
    country_b16.config(command=userchoice_countryb16)
    country_b17.place(x=151, y=567,width=113, height=51)
    country_b17.config(command=userchoice_countryb17)
    country_b18.place(x=277, y=567,width=113, height=51)
    country_b18.config(command=userchoice_countryb18)
    country_b19.place(x=136, y=633,width=146, height=48)
    country_b19.config(command=confirm_country)

'''按下"國家選單"後
a.消除介面上「所有的」對話框
b.要新增的對話框(很多)'''
def clr2crt2_country():
    clear2_country()
    clear2_forall()
    create2_country()

#選"國家"後新增的對話框
def create_country():
    country_chose.place(x=306, y=523,width=80, height=40)
    country_menu_b.place(x=121, y=632,width=260, height=40)
    secondquestion_country.place(x=21, y=565,width=243, height=50)
    country_menu_b.config(command=clr2crt2_country)
    
# 選"國家"後原來的按鈕不要+上移
def clear1_country():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_country()
    moveup()

'''地區函數區'''
# 按下"確定"，現有對話框全部消失，跳到最後對話框
def confirm_region():
    clear2_forall()
    region_l1.destroy()
    region_l2.destroy()
    region_l3.destroy()
    region_b1.destroy()
    region_b2.destroy()
    region_b3.destroy()
    region_confirm.destroy()
    region_chose.destroy()
    secondquestion_region.destroy()
    multichoice_label.destroy()
    lastmove()

# 按下某地區按鈕後，原按鈕消失，變標籤，傳入keyword
def clear2_regionb1():
    region_b1.destroy()
    region_l1.place(x=123, y=632,width=82, height=40)
    keyword.append('溫州街')
def clear2_regionb2():
    region_b2.destroy()
    region_l2.place(x=212, y=632,width=82, height=40)
    keyword.append('後門')
def clear2_regionb3():
    region_b3.destroy()
    region_l3.place(x=303, y=632,width=82, height=40)
    keyword.append('公館')

# 選"地區"後新增的對話框
def create_region():
    region_chose.place(x=306, y=523,width=80, height=40)
    region_b1.place(x=123, y=632,width=82, height=40)
    region_b1.config(command=clear2_regionb1)
    region_b2.place(x=212, y=632,width=82, height=40)
    region_b2.config(command=clear2_regionb2)
    region_b3.place(x=303, y=632,width=82, height=40)
    region_b3.config(command=clear2_regionb3)
    secondquestion_region.place(x=21, y=565,width=230, height=50)
    multichoice_label.place(x=265, y=595,width=39, height=17)
    region_confirm.place(x=50, y=642, width=60, height=30)
    region_confirm.config(command=confirm_region)

# 選"地區"後原來的按鈕不要+上移
def clear1_region():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_region()
    moveup()

'''價錢函數區'''
# 按下任何價錢皆會消失的對話框們
def clear2_price():
    clear2_forall()
    price_chose.destroy()
    secondquestion_price.destroy()
    price_b1.destroy()
    price_b2.destroy()
    price_b3.destroy()
    price_b4.destroy()
    price_b5.destroy()
    price_b6.destroy()
    price_b7.destroy()
    price_b8.destroy()

# 按下某價錢按鈕後，介面跳到最後，這是單選；傳入keyword
def clear2_priceb1():
    clear2_price()
    global upperbound
    upperbound = '100'
    lastmove()
def clear2_priceb2():
    clear2_price()
    global upperbound
    upperbound = '200'
    lastmove()
def clear2_priceb3():
    clear2_price()
    global upperbound
    upperbound = '300'
    lastmove()
def clear2_priceb4():
    clear2_price()
    global upperbound
    upperbound = '400'
    lastmove()
def clear2_priceb5():
    clear2_price()
    global upperbound
    upperbound = '500'
    lastmove()
def clear2_priceb6():
    clear2_price()
    global upperbound
    upperbound = '600'
    lastmove()
def clear2_priceb7():
    clear2_price()
    global upperbound
    upperbound = '700'
    lastmove()
def clear2_priceb8():
    clear2_price()
    global upperbound
    upperbound = '801'
    lastmove()

# 按下"價錢"後，原對話上移，但其實是重新建造新對話框
def moveup_price():
    firstquestion_c.place(x=21, y=267,width=198, height=50)
    price_b_c.place(x=126, y=324,width=80, height=40)
    category_b_c.place(x=216, y=324,width=80, height=40)
    value_b_c.place(x=306, y=324,width=80, height=40)     
    muti_b_c.place(x=306, y=377,width=80, height=40)
    country_b_c.place(x=216, y=377,width=80, height=40)
    region_b_c.place(x=126, y=377,width=80, height=40)

# 選"價錢"後新增的對話框
def create_price():
    price_chose.place(x=306, y=430,width=80, height=40)
    price_b1.place(x=126, y=529,width=82, height=40)
    price_b1.config(command=clear2_priceb1)
    price_b2.place(x=216, y=529,width=82, height=40)
    price_b2.config(command=clear2_priceb2)
    price_b3.place(x=306, y=529,width=82, height=40)
    price_b3.config(command=clear2_priceb3)
    price_b4.place(x=126, y=582,width=82, height=40)
    price_b4.config(command=clear2_priceb4)
    price_b5.place(x=216, y=582,width=82, height=40)
    price_b5.config(command=clear2_priceb5)
    price_b6.place(x=306, y=582,width=82, height=40)
    price_b6.config(command=clear2_priceb6)
    price_b7.place(x=216, y=632,width=82, height=40)
    price_b7.config(command=clear2_priceb7)
    price_b8.place(x=306, y=632,width=82, height=40)
    price_b8.config(command=clear2_priceb8)
    secondquestion_price.place(x=21, y=466,width=243, height=50)

# 選"地區"後原來的按鈕不要
def clear1_price():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_price()
    moveup_price()

'''評價函數區'''
# 按下任何評價皆會消失的對話框們
def clear2_value():
    clear2_forall()
    value_chose.destroy()
    secondquestion_value.destroy()
    value_b1.destroy()
    value_b2.destroy()
    value_b3.destroy()
    value_b4.destroy()
    value_b5.destroy()

# 按下某價錢按鈕後，介面跳到最後，這是單選；傳入keyword
def clear2_valueb1():
    clear2_value()
    global lowerbound
    lowerbound = '1'
    lastmove()
def clear2_valueb2():
    clear2_value()
    global lowerbound
    lowerbound = '2'
    lastmove()
def clear2_valueb3():
    clear2_value()
    global lowerbound
    lowerbound = '3'
    lastmove()
def clear2_valueb4():
    clear2_value()
    global lowerbound
    lowerbound = '4'
    lastmove()
def clear2_valueb5():
    clear2_value()
    global lowerbound
    lowerbound = '5'
    lastmove()

# 按下"評價"後，原對話上移，但其實是重新建造新對話框
def moveup_value():
    firstquestion_c.place(x=21, y=324,width=198, height=50)
    price_b_c.place(x=126, y=380,width=80, height=40)
    category_b_c.place(x=216, y=380,width=80, height=40)
    value_b_c.place(x=306, y=380,width=80, height=40)     
    muti_b_c.place(x=306, y=433,width=80, height=40)
    country_b_c.place(x=216, y=433,width=80, height=40)
    region_b_c.place(x=126, y=433,width=80, height=40)

# 選"評價"後新增的對話框
def create_value():
    value_chose.place(x=306, y=483,width=80, height=40)
    value_b1.place(x=126, y=584,width=82, height=40)
    value_b1.config(command=clear2_valueb1)
    value_b2.place(x=216, y=584,width=82, height=40)
    value_b2.config(command=clear2_valueb2)
    value_b3.place(x=306, y=584,width=82, height=40)
    value_b3.config(command=clear2_valueb3)
    value_b4.place(x=216, y=632,width=82, height=40)
    value_b4.config(command=clear2_valueb4)
    value_b5.place(x=306, y=632,width=82, height=40)
    value_b5.config(command=clear2_valueb5)
    secondquestion_value.place(x=21, y=519,width=238, height=50)

# 選"評價"後原來的按鈕不要
def clear1_value():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_value()
    moveup_value()


'''種類（特別為了複選）函數區'''

# 按了某種類之後，變顏色，傳出keyword給演算法(不變成標籤，太麻煩；不給重複按，太麻煩)
def userchoice_typeb1():
    type_b1.config(bg='coral', fg='white')
    keyword.append('義大利麵')
def userchoice_typeb2():
    type_b2.config(bg='coral', fg='white')
    keyword.append('咖哩飯')
def userchoice_typeb3():
    type_b3.config(bg='coral', fg='white')
    keyword.append('早午餐')
def userchoice_typeb4():
    type_b4.config(bg='coral', fg='white')
    keyword.append('河粉')
def userchoice_typeb5():
    type_b5.config(bg='coral', fg='white')
    keyword.append('飯類')
def userchoice_typeb6():
    type_b6.config(bg='coral', fg='white')
    keyword.append('麵類')
def userchoice_typeb7():
    type_b7.config(bg='coral', fg='white')
    keyword.append('火鍋')
def userchoice_typeb8():
    type_b8.config(bg='coral', fg='white')
    keyword.append('水餃')
def userchoice_typeb9():
    type_b9.config(bg='coral', fg='white')
    keyword.append('披薩')
def userchoice_typeb10():
    type_b10.config(bg='coral', fg='white')
    keyword.append('燉飯')
def userchoice_typeb11():
    type_b11.config(bg='coral', fg='white')
    keyword.append('排餐')
def userchoice_typeb12():
    type_b12.config(bg='coral', fg='white')
    keyword.append('早餐')
def userchoice_typeb13():
    type_b13.config(bg='coral', fg='white')
    keyword.append('素食')
def userchoice_typeb14():
    type_b14.config(bg='coral', fg='white')
    keyword.append('漢堡')
def userchoice_typeb15():
    type_b15.config(bg='coral', fg='white')
    keyword.append('沙拉')
def userchoice_typeb16():
    type_b16.config(bg='coral', fg='white')
    keyword.append('飯糰')
def userchoice_typeb17():
    type_b17.config(bg='coral', fg='white')
    keyword.append('炸物')
def userchoice_typeb18():
    type_b18.config(bg='coral', fg='white')
    keyword.append('粥')
def userchoice_typeb19():
    type_b19.config(bg='coral', fg='white')
    keyword.append('吐司麵包')
def userchoice_typeb20():
    type_b20.config(bg='coral', fg='white')
    keyword.append('烤肉')
def userchoice_typeb21():
    type_b21.config(bg='coral', fg='white')
    keyword.append('便當')
def userchoice_typeb22():
    type_b22.config(bg='coral', fg='white')
    keyword.append('蛋包飯')
def userchoice_typeb23():
    type_b23.config(bg='coral', fg='white')
    keyword.append('關東煮')
def userchoice_typeb24():
    type_b24.config(bg='coral', fg='white')
    keyword.append('滷味')
def userchoice_typeb25():
    type_b25.config(bg='coral', fg='white')
    keyword.append('壽喜燒')
def userchoice_typeb26():
    type_b26.config(bg='coral', fg='white')
    keyword.append('咖啡廳')
def userchoice_typeb27():
    type_b27.config(bg='coral', fg='white')
    keyword.append('甜點')
def userchoice_typeb28():
    type_b28.config(bg='coral', fg='white')
    keyword.append('冰品')
def userchoice_typeb29():
    type_b29.config(bg='coral', fg='white')
    keyword.append('鹹食')

# 按下"確定"後把當前所有按鈕標籤清理掉+跳回複數篩選
def confirm_type_formulti():
    type_label_1.place_forget()
    multichoice_label_1.place_forget()
    type_b1.place_forget()
    type_b2.place_forget()
    type_b3.place_forget()
    type_b4.place_forget()
    type_b5.place_forget()
    type_b6.place_forget()
    type_b7.place_forget()
    type_b8.place_forget()
    type_b9.place_forget()
    type_b10.place_forget()
    type_b11.place_forget()
    type_b12.place_forget()
    type_b13.place_forget()
    type_b14.place_forget()
    type_b15.place_forget()
    type_b16.place_forget()
    type_b17.place_forget()
    type_b18.place_forget()
    type_b19.place_forget()
    type_b20.place_forget()
    type_b21.place_forget()
    type_b22.place_forget()
    type_b23.place_forget()
    type_b24.place_forget()
    type_b25.place_forget()
    type_b26.place_forget()
    type_b27.place_forget()
    type_b28.place_forget()
    type_b29.place_forget()
    type_b30.place_forget()
    create_muti()

# 按下"種類選單"後要新增的按鈕們
def create2_type_formulti():
    type_label_1.place(x=38, y=102,width=46, height=40)
    multichoice_label_1.place(x=38, y=145,width=39, height=17)
    type_b1.place(x=34, y=172,width=91, height=37)
    type_b1.config(command=userchoice_typeb1)
    type_b2.place(x=160, y=172,width=91, height=37)
    type_b2.config(command=userchoice_typeb2)
    type_b3.place(x=283, y=172,width=91, height=37)
    type_b3.config(command=userchoice_typeb3)
    type_b4.place(x=34, y=219,width=91, height=37)
    type_b4.config(command=userchoice_typeb4)
    type_b5.place(x=160, y=219,width=91, height=37)
    type_b5.config(command=userchoice_typeb5)
    type_b6.place(x=283, y=219,width=91, height=37)
    type_b6.config(command=userchoice_typeb6)
    type_b7.place(x=34, y=265,width=91, height=37)
    type_b7.config(command=userchoice_typeb7)
    type_b8.place(x=160, y=265,width=91, height=37)
    type_b8.config(command=userchoice_typeb8)
    type_b9.place(x=283, y=265,width=91, height=37)
    type_b9.config(command=userchoice_typeb9)
    type_b10.place(x=34, y=312,width=91, height=37)
    type_b10.config(command=userchoice_typeb10)
    type_b11.place(x=160, y=312,width=91, height=37)
    type_b11.config(command=userchoice_typeb11)
    type_b12.place(x=283, y=312,width=91, height=37)
    type_b12.config(command=userchoice_typeb12)
    type_b13.place(x=34, y=358, width=91, height=37)
    type_b13.config(command=userchoice_typeb13)
    type_b14.place(x=160, y=358, width=91, height=37)
    type_b14.config(command=userchoice_typeb14)
    type_b15.place(x=283, y=358, width=91, height=37)
    type_b15.config(command=userchoice_typeb15)
    type_b16.place(x=34, y=405, width=91, height=37)
    type_b16.config(command=userchoice_typeb16)
    type_b17.place(x=160, y=405, width=91, height=37)
    type_b17.config(command=userchoice_typeb17)
    type_b18.place(x=283, y=405, width=91, height=37)
    type_b18.config(command=userchoice_typeb18)
    type_b19.place(x=34, y=451, width=91, height=37)
    type_b19.config(command=userchoice_typeb19)
    type_b20.place(x=160, y=451, width=91, height=37)
    type_b20.config(command=userchoice_typeb20)
    type_b21.place(x=283, y=451, width=91, height=37)
    type_b21.config(command=userchoice_typeb21)
    type_b22.place(x=34, y=498,width=91, height=37)
    type_b22.config(command=userchoice_typeb22)
    type_b23.place(x=160, y=498,width=91, height=37)
    type_b23.config(command=userchoice_typeb23)
    type_b24.place(x=283, y=498,width=91, height=37)
    type_b24.config(command=userchoice_typeb24)
    type_b25.place(x=34, y=544,width=91, height=37)
    type_b25.config(command=userchoice_typeb25)
    type_b26.place(x=160, y=544,width=91, height=37)
    type_b26.config(command=userchoice_typeb26)
    type_b27.place(x=283, y=544,width=91, height=37)
    type_b27.config(command=userchoice_typeb27)
    type_b28.place(x=34, y=591,width=91, height=37)
    type_b28.config(command=userchoice_typeb28)
    type_b29.place(x=160, y=591, width=91, height=37)
    type_b29.config(command=userchoice_typeb29)
    type_b30.place(x=156, y=638,width=102, height=49)
    type_b30.config(command=confirm_type_formulti)


'''按下"種類選單"後
a.消除介面上「所有的」對話框
b.要新增的對話框(很多)'''
def clr2crt2_type_formulti():
    filter_label.place_forget()
    type_label.place_forget()
    country_label.place_forget()
    region_label.place_forget()
    price_label.place_forget()
    value_label.place_forget()
    type_menu_b.place_forget()
    country_menu_b.place_forget()
    region_b1.place_forget()
    region_b2.place_forget()
    region_b3.place_forget()
    price_b1.place_forget()
    price_b2.place_forget()
    price_b3.place_forget()
    price_b4.place_forget()
    price_b5.place_forget()
    price_b6.place_forget()
    price_b7.place_forget()
    price_b8.place_forget()
    value_b1.place_forget()
    value_b2.place_forget()
    value_b3.place_forget()
    value_b4.place_forget()
    value_b5.place_forget()
    confirm_b.place_forget()
    create2_type_formulti()
   
    
'''國家（特別為了複選）函數區'''


# 按了料理之後，變顏色，傳出keyword給演算法(不變成標籤，太麻煩；不給重複按，太麻煩)
def userchoice_countryb1():
    country_b1.config(bg='coral', fg='white')
    keyword.append('日式壽司')
def userchoice_countryb2():
    country_b2.config(bg='coral', fg='white')
    keyword.append('日式丼飯')
def userchoice_countryb3():
    country_b3.config(bg='coral', fg='white')
    keyword.append('日式拉麵')
def userchoice_countryb4():
    country_b4.config(bg='coral', fg='white')
    keyword.append('韓式料理')
def userchoice_countryb5():
    country_b5.config(bg='coral', fg='white')
    keyword.append('中東料理')
def userchoice_countryb6():
    country_b6.config(bg='coral', fg='white')
    keyword.append('印度料理')
def userchoice_countryb7():
    country_b7.config(bg='coral', fg='white')
    keyword.append('港式料理')
def userchoice_countryb8():
    country_b8.config(bg='coral', fg='white')
    keyword.append('越式料理')
def userchoice_countryb9():
    country_b9.config(bg='coral', fg='white')
    keyword.append('泰式料理')
def userchoice_countryb10():
    country_b10.config(bg='coral', fg='white')
    keyword.append('俄羅斯料理')
def userchoice_countryb11():
    country_b11.config(bg='coral', fg='white')
    keyword.append('地中海料理')
def userchoice_countryb12():
    country_b12.config(bg='coral', fg='white')
    keyword.append('馬來西亞料理')
def userchoice_countryb13():
    country_b13.config(bg='coral', fg='white')
    keyword.append('雲南料理')
def userchoice_countryb14():
    country_b14.config(bg='coral', fg='white')
    keyword.append('四川料理')
def userchoice_countryb15():
    country_b15.config(bg='coral', fg='white')
    keyword.append('南洋料理')
def userchoice_countryb16():
    country_b16.config(bg='coral', fg='white')
    keyword.append('以色列料理')
def userchoice_countryb17():
    country_b17.config(bg='coral', fg='white')
    keyword.append('加拿大料理')
def userchoice_countryb18():
    country_b18.config(bg='coral', fg='white')
    keyword.append('夏威夷生魚飯')

# 按下"確定"後把當前所有按鈕標籤清理掉+跳回複選頁面
def confirm_country_formulti():
    country_label_1.place_forget() 
    multichoice_label_1.place_forget() 
    country_b1.place_forget() 
    country_b2.place_forget() 
    country_b3.place_forget() 
    country_b4.place_forget() 
    country_b5.place_forget() 
    country_b6.place_forget() 
    country_b7.place_forget() 
    country_b8.place_forget() 
    country_b9.place_forget() 
    country_b10.place_forget() 
    country_b11.place_forget() 
    country_b12.place_forget() 
    country_b13.place_forget() 
    country_b14.place_forget() 
    country_b15.place_forget() 
    country_b16.place_forget() 
    country_b17.place_forget() 
    country_b18.place_forget() 
    country_b19.place_forget() 
    create_muti()

# 按下"國家選單"後要新增的按鈕們
def create2_country_formulti():
    country_label_1.place(x=31, y=114,width=160, height=40)
    multichoice_label_1.place(x=31, y=171,width=39, height=17)
    country_b1.place(x=26, y=212,width=113, height=51)
    country_b1.config(command=userchoice_countryb1)
    country_b2.place(x=151, y=212,width=113, height=51)
    country_b2.config(command=userchoice_countryb2)
    country_b3.place(x=277, y=212,width=113, height=51)
    country_b3.config(command=userchoice_countryb3)
    country_b4.place(x=26, y=283,width=113, height=51)
    country_b4.config(command=userchoice_countryb4)
    country_b5.place(x=151, y=283,width=113, height=51)
    country_b5.config(command=userchoice_countryb5)
    country_b6.place(x=277, y=283,width=113, height=51)
    country_b6.config(command=userchoice_countryb6)
    country_b7.place(x=26, y=354,width=113, height=51)
    country_b7.config(command=userchoice_countryb7)
    country_b8.place(x=151, y=354,width=113, height=51)
    country_b8.config(command=userchoice_countryb8)
    country_b9.place(x=277, y=354,width=113, height=51)
    country_b9.config(command=userchoice_countryb9)
    country_b10.place(x=26, y=425,width=113, height=51)
    country_b10.config(command=userchoice_countryb10)
    country_b11.place(x=151, y=425,width=113, height=51)
    country_b11.config(command=userchoice_countryb11)
    country_b12.place(x=277, y=425,width=113, height=51)
    country_b12.config(command=userchoice_countryb12)
    country_b13.place(x=26, y=496,width=113, height=51)
    country_b13.config(command=userchoice_countryb13)
    country_b14.place(x=151, y=496,width=113, height=51)
    country_b14.config(command=userchoice_countryb14)
    country_b15.place(x=277, y=496,width=113, height=51)
    country_b15.config(command=userchoice_countryb15)
    country_b16.place(x=26, y=567,width=113, height=51)
    country_b16.config(command=userchoice_countryb16)
    country_b17.place(x=151, y=567,width=113, height=51)
    country_b17.config(command=userchoice_countryb17)
    country_b18.place(x=277, y=567,width=113, height=51)
    country_b18.config(command=userchoice_countryb18)
    country_b19.place(x=136, y=633,width=146, height=48)
    country_b19.config(command=confirm_country_formulti)

'''按下"國家選單"後
a.消除介面上「所有的」對話框
b.要新增的對話框(回到國家選單那個很多選擇的頁面)'''
def clr2crt2_country_formulti():
    filter_label.place_forget()
    type_label.place_forget()
    country_label.place_forget()
    region_label.place_forget()
    price_label.place_forget()
    value_label.place_forget()
    type_menu_b.place_forget()
    country_menu_b.place_forget()
    region_b1.place_forget()
    region_b2.place_forget()
    region_b3.place_forget()
    price_b1.place_forget()
    price_b2.place_forget()
    price_b3.place_forget()
    price_b4.place_forget()
    price_b5.place_forget()
    price_b6.place_forget()
    price_b7.place_forget()
    price_b8.place_forget()
    value_b1.place_forget()
    value_b2.place_forget()
    value_b3.place_forget()
    value_b4.place_forget()
    value_b5.place_forget()
    confirm_b.place_forget()
    create2_country_formulti()


'''複選函數區'''
#價錢、地區、評價存入keyword

def userchoice_region_b1():
    region_b1.config(bg='coral', fg='white')
    keyword.append('溫州街')
def userchoice_region_b2():
    region_b2.config(bg='coral', fg='white')
    keyword.append('後門')
def userchoice_region_b3():
    region_b3.config(bg='coral', fg='white')
    keyword.append('公館')
def userchoice_price_b1():
    price_b1.config(bg='coral', fg='white')
    global upperbound
    upperbound = '100'
def userchoice_price_b2():
    price_b2.config(bg='coral', fg='white')
    global upperbound
    upperbound = '200'
def userchoice_price_b3():
    price_b3.config(bg='coral', fg='white')
    global upperbound
    upperbound = '300'
def userchoice_price_b4():
    price_b4.config(bg='coral', fg='white')
    global upperbound
    upperbound = '400'
def userchoice_price_b5():
    price_b5.config(bg='coral', fg='white')
    global upperbound
    upperbound = '500'
def userchoice_price_b6():
    price_b6.config(bg='coral', fg='white')
    global upperbound
    upperbound = '600'
def userchoice_price_b7():
    price_b7.config(bg='coral', fg='white')
    global upperbound
    upperbound = '700'
def userchoice_price_b8():
    price_b8.config(bg='coral', fg='white')
    global upperbound
    upperbound = '801'
def userchoice_value_b1():
    value_b1.config(bg='coral', fg='white')
    global lowerbound
    lowerbound = '1'
def userchoice_value_b2():
    value_b2.config(bg='coral', fg='white')
    global lowerbound
    lowerbound = '2'
def userchoice_value_b3():
    value_b3.config(bg='coral', fg='white')
    global lowerbound
    lowerbound = '3'
def userchoice_value_b4():
    value_b4.config(bg='coral', fg='white')
    global lowerbound
    lowerbound = '4'
def userchoice_value_b5():
    value_b5.config(bg='coral', fg='white')
    global lowerbound
    lowerbound = '5'



# 按下"確定"後把當前所有按鈕標籤清理掉+跳到最後畫面
def confirm_muti():
    filter_label.destroy()
    type_label.destroy()
    country_label.destroy()
    region_label.destroy()
    price_label.destroy()
    value_label.destroy()
    type_menu_b.destroy()
    country_menu_b.destroy()
    region_b1.destroy()
    region_b2.destroy()
    region_b3.destroy()
    price_b1.destroy()
    price_b2.destroy()
    price_b3.destroy()
    price_b4.destroy()
    price_b5.destroy()
    price_b6.destroy()
    price_b7.destroy()
    price_b8.destroy()
    value_b1.destroy()
    value_b2.destroy()
    value_b3.destroy()
    value_b4.destroy()
    value_b5.destroy()
    confirm_b.destroy()
    lastmove()


#選"複選"後新增的頁面
def create_muti():
    filter_label.place(x=31, y=65)
    type_label.place(x=31, y=100)
    country_label.place(x=31, y=182)
    region_label.place(x=31, y=276)
    price_label.place(x=31, y=369)
    value_label.place(x=31, y=513)
    type_menu_b.place(x=31, y=126,width=196, height=44)
    type_menu_b.config(command=clr2crt2_type_formulti)
    country_menu_b.place(x=31, y=220,width=196, height=44)
    country_menu_b.config(command=clr2crt2_country_formulti)
    region_b1.place(x=31, y=311,width=82, height=44)
    region_b1.config(command=userchoice_region_b1)
    region_b2.place(x=132, y=311,width=82, height=44)
    region_b2.config(command=userchoice_region_b2)
    region_b3.place(x=232, y=311,width=82, height=44)
    region_b3.config(command=userchoice_region_b3)
    price_b1.place(x=31, y=404,width=82, height=40)
    price_b1.config(command=userchoice_price_b1)
    price_b2.place(x=121, y=404,width=82, height=40)
    price_b2.config(command=userchoice_price_b2)    
    price_b3.place(x=217, y=404,width=82, height=40)
    price_b3.config(command=userchoice_price_b3)    
    price_b4.place(x=312, y=404,width=82, height=40)
    price_b4.config(command=userchoice_price_b4)    
    price_b5.place(x=31, y=455,width=82, height=40)
    price_b5.config(command=userchoice_price_b5)    
    price_b6.place(x=121, y=455,width=82, height=40)
    price_b6.config(command=userchoice_price_b6)    
    price_b7.place(x=217, y=455,width=82, height=40)
    price_b7.config(command=userchoice_price_b7)    
    price_b8.place(x=312, y=455,width=82, height=40)
    price_b8.config(command=userchoice_price_b8)    
    value_b1.place(x=31, y=548,width=60, height=40)
    value_b1.config(command=userchoice_value_b1)    
    value_b2.place(x=106, y=548,width=60, height=40)
    value_b2.config(command=userchoice_value_b2)    
    value_b3.place(x=182, y=548,width=60, height=40)
    value_b3.config(command=userchoice_value_b3)    
    value_b4.place(x=257, y=548,width=60, height=40)
    value_b4.config(command=userchoice_value_b4)    
    value_b5.place(x=332, y=548,width=60, height=40)
    value_b5.config(command=userchoice_value_b5)    
    confirm_b.place(x=163, y=627,width=94, height=46)   
    confirm_b.config(command=confirm_muti)
    
    
# 選"複選"後原來的按鈕不要+上移，直接進入複選選單的頁面
def clear1_muti():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_muti()


# 選擇"種類"後要執行的函數
category_b.config(command=clear1_type)
# 選擇"國家"後要執行的函數
country_b.config(command=clear1_country)
# 選擇"地區"後要執行的函數
region_b.config(command=clear1_region)
# 選擇"價錢"後要執行的函數
price_b.config(command=clear1_price)
# 選擇"評價"後要執行的函數
value_b.config(command=clear1_value)
# 選擇"複選"後要執行的函數
muti_b.config(command=clear1_muti)


window.mainloop()
print('keyword', keyword)
print('upperbound', upperbound)
print('lowerbound', lowerbound)

# 建立商家 class
class Store:
    def __init__(self, name, lon, lat, avg_ranking, lowerbound, upperbound, area, types):
        self.name = name                       # 名稱
        self.lon = float(lon)                  # 經度
        self.lat = float(lat)                  # 緯度
        self.avg_ranking = float(avg_ranking)  # 平均評價星等
        self.lowerbound = int(lowerbound)      # 價錢區間下界
        self.upperbound = int(upperbound)      # 價錢區間上界
        self.area = area                       # 區域
        self.types = types                     # 種類 (是一個清單)
        # self.keys = keys                       # 關鍵字

    def __str__(self):
        return str(self.name)


# 所有商家清單
stores = list()

# 記得改成存檔案的地方
filepath = r'C:\\Users\\JasonChen\\Desktop\\github\\pbc~final\\store_info_final.csv'

with open(file=filepath, mode='r', encoding='utf-8', newline='') as csvfile:
    rows = csv.reader(csvfile)
    rows = list(rows)

    for i in range(0, len(rows), 2): 
        # 將價格區間切分為上界和下界儲存
        price_intl = rows[i][4].split('-')
        # 轉成 store 類別存入 stores 清單
        stores.append(Store(rows[i][0], rows[i][1], rows[i][2], rows[i][3], price_intl[0],
                            price_intl[1], rows[i][5], rows[i][6:len(rows[i])]))


# 定義過濾函式
# 傳入待過濾的 商家清單 以及 關鍵字清單
# 這裡是聯集概念
def filter1(store_list, keywords_list):
    # 新增一個空清單

    done = list()

    for keyword in keywords_list:
        # 檢查每一間商家是否符合條件，符合條件的加入 done 清單
        if keyword in ['溫州街', '公館', '後門']:
            # 如果關鍵字是區域
            for store in store_list:
                if store.area == keyword:
                    done.append(store)
        else:
            for store in store_list:
                if (keyword != '飯類') and (keyword != '麵類'):
                    if keyword in store.types:
                        done.append(store)
                else:
                    for each in store.types:
                        # 因為若選擇「麵類」會把有「麵包」的商家也放進來，所以要刪掉    
                        if (keyword[0] in each) and (each != '麵包'):
                            done.append(store)
                            break

    # 刪除重複商家
    done = list(set(done))

    if done != []:
        # 回傳過濾後的商家清單
        return done
    else:
        return store_list

# 定義選擇價格區間
# 傳入待過濾的 商家清單 以及 價格上界
def price_choose(store_list, upperbound):
    # 新增一個空清單
    done = list()
    if upperbound != '':
        # 轉成整數
        upperbound = int(upperbound)
        
        # 檢查每一間商家是否符合條件，符合條件的加入 done 清單
        for store in store_list:
            if store.upperbound <= upperbound:
                done.append(store)
            elif (store.upperbound > upperbound) and (store.lowerbound < upperbound):
                done.append(store)
            else:
                continue
    else:
        done = store_list
    # 回傳過濾後的商家清單
    return done


# 定義選擇評價區間
# 傳入待過濾的 商家清單 以及 評價下界
def ranking_choose(store_list, lowerbound):
    # 新增一個空清單
    done = list()
    if lowerbound != '':
        # 轉成整數
        lowerbound = int(lowerbound)
        
        # 檢查每一間商家是否符合條件，符合條件的加入 done 清單
        for store in store_list:
            if store.avg_ranking >= lowerbound:
                done.append(store)
    else:
        done = store_list
    # 回傳過濾後的商家清單
    return done


# 解決 matplotlib 中文字型問題
fpath = 'C:\\Users\\JasonChen\\Desktop\\github\\pbc~final\\jhenghei bold.ttf'
prop = fm.FontProperties(fname=fpath)


# 定義畫出地圖的函式
def food_map(store_list):

    lons = list()  # x 座標：經度
    lats = list()  # y 座標：緯度

    # 讀取商家經緯度
    for store in store_list:
        lons.append(store.lon)
        lats.append(store.lat)

    # 轉成矩陣
    lons = np.array(lons) 
    lats = np.array(lats)  

    x, y = (lons, lats) # transform coordinates 

    # 讀入地圖底圖
    img = plt.imread("C:\\Users\\JasonChen\\Desktop\\github\\pbc~final\\地圖＋畫框.png")
    # 建立畫框和圖表
    fig, ax = plt.subplots(figsize=(16, 10), dpi=70)
    # 圖表顯示地圖底圖以及設定座標軸
    ax.imshow(img, extent=[121.5136161, 121.5480002, 25.00897, 25.02854])
    # 不顯示座標軸
    # plt.axis('off')

    # 標示商家位置
    line, = ax.plot(x, y, ls="", marker='o', color='#fa4a0c') 

    # 商家資訊清單
    message_list = list()

    # 製作資訊框
    for i, store in enumerate(store_list):
        store.types = '、'.join(store.types)

        message = [store.name,
                   '[' + str(store.area) + '] ｜ ' + store.types,
                   '★ ' + str(store.avg_ranking) + ' / 5.0 ｜ ' + 'NT＄' + str(store.lowerbound) + ' ~ NT＄' + str(store.upperbound)]

        message = '\n'.join(message)

        message_list.append(message)

        message = TextArea(message, minimumdescent=False, textprops=dict(fontproperties=prop))

        xybox = (50, 50)
        ab = AnnotationBbox(message, (x[i],y[i]),
                            xybox=xybox,
                            xycoords='data',
                            boxcoords="offset points",
                            pad=0.3,
                            arrowprops=dict(arrowstyle="->"))

    # 把它放到圖表上
        ax.add_artist(ab)
    # 轉成可顯示
        ab.set_visible(False)

    # 滑鼠事件
    # 游標移到該點位置顯示文字
    def hover(event):
        # if the mouse is over the scatter points
        if line.contains(event)[0]:
            # find out the index within the array from the event
            ind, = line.contains(event)[1]["ind"]
            # get the figure size
            w,h = fig.get_size_inches()*fig.dpi
            ws = (event.x > w/2.)*-1 + (event.x <= w/2.) 
            hs = (event.y > h/2.)*-1 + (event.y <= h/2.)
            # if event occurs in the top or right quadrant of the figure,
            # change the annotation box position relative to mouse.
            ab.xybox = (xybox[0]*ws, xybox[1]*hs)
            # make annotation box visible
            ab.set_visible(True)
            # place it at the position of the hovered scatter point
            ab.xy =(x[ind], y[ind])
            # set the image corresponding to that point
            message.set_text(message_list[ind])
        else:
            #if the mouse is not over a scatter point
            ab.set_visible(False)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('motion_notify_event', hover)

    plt.show()

'''連在一起：從介面傳入篩選的東西經過演算法跑出所有符合的店家名稱；
三個函數過濾是取交集(filter1內部是聯集)'''
a = filter1(stores, keyword)
b = price_choose(a, upperbound)
c = ranking_choose(b, lowerbound)

for store in c:
    print(store)

food_map(c)
