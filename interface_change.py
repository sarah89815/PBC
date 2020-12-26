# coding: utf-8

# 引入套件
from PIL import ImageTk,Image
from tkinter import CENTER, NW, TOP
import tkinter as tk

# 建keyword清單
keyword = list()

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
還沒"place"所以還不會出現。在後面有新寫到的都要補在這裡！'''
firstquestion_c = tk.Label(window, text='你今天想吃什麼呢？', bg='lightgrey' ,font=('Helvetica Neue','15'), fg = 'black')
# 為了讓使用者不再重複點種類或國家那些的，變成label
price_b_c = tk.Label(window, text='價錢', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
category_b_c = tk.Label(window, text='種類', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
muti_b_c = tk.Label(window, text='複選', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
value_b_c = tk.Label(window, text='評價', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
country_b_c = tk.Label(window, text='國家', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
region_b_c = tk.Label(window, text='地區', font=('Helvetica Neue', 15), bg='#ED9A47', fg='white')
# 最後一個對話框
finish = tk.Label(window, text='我幫你找到符合條件的餐廳了！\n \n可以移動游標到圖釘了解餐廳資訊喔', font=('Helvetica Neue', 12), bg='lightgrey', fg='black')
# type線的部分
secondquestion_type = tk.Label(window, text='你會想要甚麼種類呢？', bg='lightgrey',font=('Helvetica Neue',15), fg = 'black')
category_chose = tk.Label(window, text='種類', bg='lightgrey' ,font=('Helvetica Neue', 15), fg='black')
category_menu_b= tk.Button(window, bg='orangered', fg="white", text='種類選單', font=('Helvetica Neue', 18))
# country線的部分
secondquestion_country = tk.Label(window, text='你會想要哪國的料理呢？', bg='lightgrey' ,font=('Helvetica Neue',15), fg = 'black')
country_chose = tk.Label(window, text='國家', bg='lightgrey',font=('Helvetica Neue', 15), fg='black')
country_menu_b= tk.Button(window, bg='orangered', fg="white", text='異國料理種類選單', font=('Helvetica Neue', 18))
country_label = tk.Label(window, text='異國料理種類', bg='white', font=('Helvetica Neue',19), fg='grey')
multichoice_label = tk.Label(window, text='可複選', bg='white', font=('Helvetica Neue',10), fg='lightgrey')
country_b1 = tk.Button(window, text='日式壽司', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b2 = tk.Button(window, text='日式丼飯', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b3 = tk.Button(window, text='日式拉麵', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b4 = tk.Button(window, text='韓式料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b5 = tk.Button(window, text='中東料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b6 = tk.Button(window, text='印度料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b7 = tk.Button(window, text='港式料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b8 = tk.Button(window, text='越式料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b9 = tk.Button(window, text='泰式料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b10 = tk.Button(window, text='俄羅斯料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b11 = tk.Button(window, text='地中海料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b12 = tk.Button(window, text='馬來西亞料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b13 = tk.Button(window, text='雲南料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b14 = tk.Button(window, text='四川料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b15 = tk.Button(window, text='南洋料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b16 = tk.Button(window, text='以色列料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b17 = tk.Button(window, text='加拿大料理', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b18 = tk.Button(window, text='夏威夷生魚飯', bg='lightgrey', fg='black', font=('Helvetica Neue', 13))
country_b19 = tk.Button(window, text='確定', bg='orangered', fg='white', font=('Helvetica Neue', 13))

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

# 不管哪條線都相同的函數!(原對話上移，但其實是重新建造新對話框)
def moveup():
    firstquestion_c.place(x=30, y=359,width=198, height=50)
    price_b_c.place(x=126, y=416,width=80, height=40)
    category_b_c.place(x=216, y=416,width=80, height=40)
    value_b_c.place(x=306, y=416,width=80, height=40)     
    muti_b_c.place(x=306, y=470,width=80, height=40)
    country_b_c.place(x=216, y=470,width=80, height=40)
    region_b_c.place(x=126, y=470,width=80, height=40)

# 按下"確定"或是其他確認按鈕後跳出最後一個對話框+接上地圖部分
def lastmove():
    finish.place(x=35, y=330,width=345, height=91)

'''種類函數區'''
# 按下"種類選單"後消除之前介面上「新增的」對話
def clear2_type():
    secondquestion_type.destroy()
    category_chose.destroy()
    category_menu_b.destroy()

# 按下"種類選單"後消除介面上「所有的」對話框
def clear2sum_type():
    clear2_type()
    clear2_forall()

#選"種類"後新增的對話框
def create_type():
    category_chose.place(x=306, y=523,width=80, height=40)
    category_menu_b.place(x=214, y=632,width=175, height=40)
    secondquestion_type.place(x=21, y=565,width=203, height=50)
    category_menu_b.config(command=clear2sum_type)

# 選"種類"後原來的按鈕不要
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
    country_b1.config(bg='orangered', fg='white')
    keyword.append('日式壽司')
def userchoice_countryb2():
    country_b2.config(bg='orangered', fg='white')
    keyword.append('日式丼飯')
def userchoice_countryb3():
    country_b3.config(bg='orangered', fg='white')
    keyword.append('日式拉麵')
def userchoice_countryb4():
    country_b4.config(bg='orangered', fg='white')
    keyword.append('韓式料理')
def userchoice_countryb5():
    country_b5.config(bg='orangered', fg='white')
    keyword.append('中東料理')
def userchoice_countryb6():
    country_b6.config(bg='orangered', fg='white')
    keyword.append('印度料理')
def userchoice_countryb7():
    country_b7.config(bg='orangered', fg='white')
    keyword.append('港式料理')
def userchoice_countryb8():
    country_b8.config(bg='orangered', fg='white')
    keyword.append('越式料理')
def userchoice_countryb9():
    country_b9.config(bg='orangered', fg='white')
    keyword.append('泰式料理')
def userchoice_countryb10():
    country_b10.config(bg='orangered', fg='white')
    keyword.append('俄羅斯料理')
def userchoice_countryb11():
    country_b11.config(bg='orangered', fg='white')
    keyword.append('地中海料理')
def userchoice_countryb12():
    country_b12.config(bg='orangered', fg='white')
    keyword.append('馬來西亞料理')
def userchoice_countryb13():
    country_b13.config(bg='orangered', fg='white')
    keyword.append('雲南料理')
def userchoice_countryb14():
    country_b14.config(bg='orangered', fg='white')
    keyword.append('四川料理')
def userchoice_countryb15():
    country_b15.config(bg='orangered', fg='white')
    keyword.append('南洋料理')
def userchoice_countryb16():
    country_b16.config(bg='orangered', fg='white')
    keyword.append('以色列料理')
def userchoice_countryb17():
    country_b17.config(bg='orangered', fg='white')
    keyword.append('加拿大料理')
def userchoice_countryb18():
    country_b18.config(bg='orangered', fg='white')
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
    secondquestion_country.place(x=21, y=565,width=230, height=50)
    country_menu_b.config(command=clr2crt2_country)
    
# 選"國家"後原來的按鈕不要
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

# 選擇"種類"後要執行的函數
category_b.config(command=clear1_type)
# 選擇"國家"後要執行的函數
country_b.config(command=clear1_country)










window.mainloop()