cd /Users/tienying/Desktop/介面圖壓縮

# 引入套件
import tkinter as tk
from PIL import ImageTk, Image

# 建立地圖和 Frame（把元件變成群組的容器）
window = tk.Tk()
top_frame = tk.Frame(window)
window.title('吃台大小幫手地圖')
window.geometry("1300x810")
#canvas = tk.Canvas(window, bg='green', height=800, width=1280)
mapscreenImage = tk.PhotoImage(file='地圖＋畫框.png')  # 圖片位置（相對路徑，與.py檔案同一資料夾下，也可以用絕對路徑，需要給定圖片具體絕對路徑）
mapscreenFrame = tk.Frame(window, width=1280, height = 800,)
mapscreenFrame.place()
mapscreenLabel = tk.Label(mapscreenFrame, image=mapscreenImage)
#image = canvas.create_image(640, 0, anchor='n',image=image_file)        # 圖片錨定點（n圖片頂端的中間點位置）放在畫布（25
mapscreenLabel.place()
# 運行主程式
window.mainloop()



#對話框視窗

window = tk.Tk()
window.title('對話')

# 第3步，設定視窗的大小(長 * 寬)
# 基本元素
window.title('吃台大小幫手')
window.geometry("414x700")

# 不給使用者動大小
window.resizable(False, False)
window.geometry("414x700")  # 這裡的乘是小x
window.minsize(width = 414, height =700)
window.configure(background="white")

# 第4步，在圖形介面上設定標籤
banner = tk.Label(window, text='吃台大小幫手', bg='lightgrey' ,font=('Helvetica Neue','19'), fg = 'black')
# 說明： bg為背景，font為字型，width為長，height為高，這裡的長和高是字元的長和高，比如height=2,就是標籤有2個字元這麼高
# 第5步，放置標籤
banner.place(x=0, y=0,width=414, height=74)    # Label內容content區域放置位置，自動調節尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();



# 建立你要吃什麼那個圖
firstquestion = tk.Label(window, text='你今天想吃什麼呢？', bg='lightgrey' ,font=('Helvetica Neue','19'), fg = 'black')
firstquestion.place(x=30, y=500,width=198, height=40)


price_b = tk.Button(window,bg='orangered',text='價錢', font=('Helvetica Neue', 18)) 
price_b.config(bg="orangered")
price_b.place(x=126, y=572,width=80, height=40)
category_b = tk.Button(window,bg='orangered',text='種類', font=('Helvetica Neue', 18))
category_b.place(x=216, y=572,width=80, height=40)
category_b.config(bg="orangered")
value_b = tk.Button(window,bg='orangered',text='評價', font=('Helvetica Neue', 18))
value_b.place(x=306, y=572,width=80, height=40)
value_b.config(bg="orangered")
muti_b = tk.Button(window,bg='orangered',text='複選', font=('Helvetica Neue', 18))      
muti_b.place(x=306, y=625,width=80, height=40)
muti_b.config(bg="orangered")
country_b = tk.Button(window,bg='orangered',text='國家', font=('Helvetica Neue', 18))
country_b.place(x=216, y=625,width=80, height=40)
country_b.config(bg="orangered")
region_b = tk.Button(window,bg='orangered',text='地區', font=('Helvetica Neue', 18))
region_b.place(x=126, y=625,width=80, height=40)
region_b.config(bg="orangered")

# 清除掉對話框的頁面
def clear2():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    category_chose.destroy()
    #creat_category__menu()
#def creat_category__menu():
    
#建立選擇種類後你想要什麼種類的圖
def create_category():
    category_chose = tk.Label(window, text='種類', bg='orangered' ,font=('Helvetica Neue','19'), fg = 'white')
    category_chose.place(x=306, y=523,width=80, height=40)
    category_menu_b= tk.Button(window,bg='orangered',text='種類選單', font=('Helvetica Neue', 18))
    category_menu_b.place(x=214, y=632,width=175, height=40)
    category_menu_b.config(command=clear2)
        #上移動往上位移
    firstquestion = tk.Label(window, text='你今天想吃什麼呢？', \
                             bg='lightgrey' ,font=('Helvetica Neue','19'), fg = 'black')
    firstquestion.place(x=30, y=359,width=200, height=40)
    categoryquestion = tk.Label(window, text='你會想要什麼種類呢', \
                                bg='lightgrey' ,font=('Helvetica Neue','19'), fg = 'black')
    categoryquestion.place(x=30, y=565,width=200, height=40)
    # 第5步，在視窗介面設定放置Button按鍵
    price_b = tk.Button(window,bg='orangered',text='價錢', font=('Helvetica Neue', 18)) 
    price_b.config(bg="orangered")
    price_b.place(x=126, y=416,width=80, height=40)
    category_b = tk.Button(window,bg='orangered',text='種類', font=('Helvetica Neue', 18))
    category_b.place(x=216, y=417,width=80, height=40)
    category_b.config(bg="orangered")
    value_b = tk.Button(window,bg='orangered',text='評價', font=('Helvetica Neue', 18))
    value_b.place(x=306, y=417,width=80, height=40)
    value_b.config(bg="orangered")
    muti_b = tk.Button(window,bg='orangered',text='複選', font=('Helvetica Neue', 18))      
    muti_b.place(x=306, y=470,width=80, height=40)
    muti_b.config(bg="orangered")
    country_b = tk.Button(window,bg='orangered',text='國家', font=('Helvetica Neue', 18))
    country_b.place(x=216, y=470,width=80, height=40)
    country_b.config(bg="orangered")
    region_b = tk.Button(window,bg='orangered',text='地區', font=('Helvetica Neue', 18))
    region_b.place(x=126, y=470,width=80, height=40)
    region_b.config(bg="orangered")

# 選種類之後原來的按鈕不要
def clear1():
    firstquestion.destroy()
    price_b.destroy()
    category_b.destroy()
    value_b.destroy()
    muti_b.destroy()      
    country_b.destroy()
    region_b.destroy()
    create_category()

#選擇種類按鈕
category_b.config(command=clear1)


window.mainloop()
