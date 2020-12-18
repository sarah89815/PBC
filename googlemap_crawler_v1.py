# coding: utf-8

# 引入函式庫
import requests 
import json
import csv
import time

# 商家資訊
time.sleep(1)
# 讀入店家資訊連結
url_1 = input("輸入 Request URL (place?authuser...)\n")

# 發送 get 請求
text_1 = requests.get(url_1).text
# 取代掉特殊字元，這個字元是為了資訊安全而設定
pretext_1 = ')]}\''
text_1 = text_1.replace(pretext_1, '')
# 把字串讀取成 json
info = json.loads(text_1)

# 追加寫入 store_info.csv 檔
# 記得改成自己存檔的位置
filepath = r'/Users/yuchiaching/Desktop/store_info.csv'

with open(file=filepath, mode='a+', encoding='utf-8', newline='') as f1:

    writer = csv.writer(f1)

    # 店名
    store_name = str(info[6][11])
    # 地址
    address = str(info[6][2][0][3:])
    # 電話
    phone_number = str(info[6][178][0][0])
    # 總評論數
    ttl_comment_cnt = str(info[6][4][8])
    # 平均星等評價
    avg_rating = str(info[6][4][7])
    # 星等分佈
    dist_rating = str(info[6][52][3])

    tmp_list_1 = [store_name, address, phone_number, ttl_comment_cnt, avg_rating, dist_rating]
    writer.writerow(tmp_list_1)


# 商家評論

# 讀入連結
tmp = input("輸入 Request URL (listentitiesreviews...)\n").split('1i0!')

store_name = store_name.strip(' ')
store_name = store_name.split(' ')
store_name = "_".join(store_name)

# 建立商家評論檔案
# 記得改成自己存檔的位置
filepath = '/Users/yuchiaching/Desktop/' + store_name + '.csv'

with open(file = filepath, mode='a+', encoding='utf-8', newline='') as f2:

    writer = csv.writer(f2)

    # 先試抓 100 則評論
    for i in range(0, 100, 10):

        # 根據連結結構，替換字串
        str_ = "1i" + str(i) + "!"    
        url_2 = str_.join(tmp)

        time.sleep(1)
        # 發送 get 請求
        text_2 = requests.get(url_2).text
        # 取代掉特殊字元，這個字元是為了資訊安全而設定
        pretext_2 = ')]}\''
        text_2 = text_2.replace(pretext_2,'')
        # 把字串讀取成 json
        soup = json.loads(text_2)
        # 取出包含留言的 List
        conlist = soup[2]

        for j in conlist:

            # 用戶名
            username = str(j[0][1])
            # 評論時間
            comment_time = str(j[1])
            # 評價星等
            rating = str(j[4])
            # 評價內容（刪除換行符號）
            comment = str(j[3])
            comment = comment.replace('\n', ' ')

            tmp_list_2 = [username, comment_time, rating, comment]
            writer.writerow(tmp_list_2)

print("\n" + str(store_name) + "\nFINISH!\n")

