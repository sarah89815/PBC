# 善心人士_1
# https://medium.com/用力去愛一個人的話-心也會痛的/默默地學-python-互動式圖像-fb25d462bb7

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
# 繪製圖片用
import os
import pygame
from PIL import ImageFont, ImageDraw, Image


# 畫出地圖的函式
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
    img = plt.imread("/Users/yuchiaching/Desktop/完稿壓縮正確尺寸/地圖＋畫框.png")
    # 建立畫框和圖表
    fig, ax = plt.subplots(figsize=(16, 10), dpi=70)
    # 圖表顯示地圖底圖以及設定座標軸
    # 善心人士_2
    # http://hk.uwenku.com/question/p-qgzudzqa-bc.html
    ax.imshow(img, extent=[121.52209923089963, 121.55634026412044, 25.00897, 25.02854])
    # 不顯示座標軸
    plt.axis('off')

    # 標示商家位置
    line, = ax.plot(x, y, ls="", marker='o', color='#fa4a0c') 


    # 圖片顯示相關
    # 待修正

    arr = np.empty((len(x),10,10))
    for i in range(len(x)):
        f = np.random.rand(5,5)
        arr[i, 0:5,0:5] = f
        arr[i, 5:,0:5] =np.flipud(f)
        arr[i, 5:,5:] =np.fliplr(np.flipud(f))
        arr[i, 0:5:,5:] = np.fliplr(f)
    # create the annotations box
    # 顯示圖片部分
    im = OffsetImage(arr[0,:,:], zoom=5)
    xybox=(50, 50)
    ab = AnnotationBbox(im, (x[0],y[0]), xybox=xybox, xycoords='data',
            boxcoords="offset points",  pad=0.3,  arrowprops=dict(arrowstyle="->"))

    # 把他放到圖表上
    ax.add_artist(im_s)
    # 轉成可顯示
    ab.set_visible(False)


    # CopyPaste
    # 滑鼠事件
    # 游標移到該點位置顯示圖片
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
            im.set_data(arr[ind,:,:])
        else:
            #if the mouse is not over a scatter point
            ab.set_visible(False)
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect('motion_notify_event', hover)

    plt.show()

    #
    return str(finish)


# 建立商家 class
# from 演算法.py
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


# 製作圖片

def text2image(store):

    # 文字內容
    store.types = '、'.join(store.types)

    message = [store.name,
               '[' + str(store.area) + '] ｜ ' + store.types,
               '★ ' + str(store.avg_ranking) + ' / 5.0 ｜ ' + 'NT$' + str(store.lowerbound) + ' ~ NT$' + str(store.upperbound)]

    # 找出最長的行數
    max_len = 0
    for str_ in message:
        if len(str_) > max_len:
            max_len = len(str_)

    # 目前長寬(幾個字元)
    length = max_len       # 長
    width = len(message)   # 寬

    # 轉成字串
    message = '\n'.join(message)

    # 可以再調整
    # size是產生的底圖大小，目前估算一個字長度約15，一行寬度約25
    im_size = (length * 15, width * 25)
    im_text = Image.new("RGB", size=im_size, color='white')


    # 產生背景圖
    im_background_raw = Image.open("/Users/yuchiaching/Desktop/GitHub/PBC_Final/text to image/food.jpg")
    im_background_edit = im_background_raw.resize(im_size, Image.ANTIALIAS)

    # 畫出底圖
    dr = ImageDraw.Draw(im_text)

    # 字型檔案路徑、字的大小
    font = ImageFont.truetype(font="/Users/yuchiaching/Desktop/GitHub/PBC_Final/text to image/jhenghei bold.ttf", size=14)

    # 在底圖上加入字串，fill可以改字的顏色
    dr.text((10, 5), message, font=font, fill="#000000")

    # 結合兩張圖 背景透明度0.3
    im = Image.blend(im_text, im_background_edit, 0.3)

    # 顯示圖片
    im.show()

    return im

# 測試資料
store = Store('小林阿盛壽司', 121.5237202, 25.0170687, 4.0, 0, 
               100, '溫州街', ['日式壽司', '麵類'])

a = text2image(store)
