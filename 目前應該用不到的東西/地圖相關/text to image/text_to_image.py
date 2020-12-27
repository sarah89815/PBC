import os
import pygame
from PIL import ImageFont, ImageDraw, Image

# 要做成圖片的字串 \n為換行符號
text = u"小林阿盛壽司\n4.0 麵、味噌湯"
row_number = text.count("\n") + 1

# 若字串不只一行，則找出長度最長那行
string_len_list = []
if text.count("\n") != 0:
    text_list = text.split('\n')
    for i in range(len(text_list)):
        string_len_list.append(len(text_list[i]))
    string_len_list.sort(reverse=True)
    column_len = string_len_list[0]
# 若字串只有一行，直接計算長度
else:
    column_len = len(text)

# size是產生的底圖大小，目前估算一個字長度約15，一行寬度約25
im_size = (column_len*15, row_number*25)
im_text = Image.new("RGB", size=im_size, color='white')

# 產生背景圖
im_background_raw = Image.open("/Users/min/Desktop/text to image/food.jpg")
im_background_edit = im_background_raw.resize(im_size, Image.ANTIALIAS)

# 畫出底圖
dr = ImageDraw.Draw(im_text)

# 字型檔案路徑、字的大小
font = ImageFont.truetype(font="/Users/min/Desktop/text to image/jhenghei bold.ttf", size=14)

# 在底圖上加入字串，fill可以改字的顏色
dr.text((10, 5),text, font=font,fill="#000000")

# 結合兩張圖 背景透明度0.3
im = Image.blend(im_text, im_background_edit, 0.3)

# 顯示圖片
im.show()

im.save("text.png")