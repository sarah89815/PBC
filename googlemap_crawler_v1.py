# coding: utf-8

# 引入函式庫
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import requests
import json
import csv
import time

name_list = list()

# 讀出商家清單
# 記得改成自己放檔案的位置
with open(file='/Users/yuchiaching/Desktop/GitHub/PBC_Final/store_info.csv', mode='r', encoding='utf-8', newline='') as f:

    rows = csv.reader(f)

  # 以迴圈輸出每一列
    for row in rows:
        name_list.append(row[0])

for store in name_list:

    # 主要用途為取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。
    options = Options()
    options.add_argument("--disable-notifications")

    # 取用 chromedriver
    # 記得改 chromedriver 的位置
    chrome = webdriver.Chrome('/Users/yuchiaching/Desktop/GitHub/PBC_Final/chromedriver', chrome_options=options)
    chrome.maximize_window()
    time.sleep(5)
    chrome.get("https://www.google.com.tw/maps")
    time.sleep(5)
    searchbox_input = chrome.find_element_by_id("searchboxinput")
    time.sleep(2)
    searchbox_input.send_keys(store)
    time.sleep(2)
    searchbox_input.send_keys(Keys.ENTER)
    time.sleep(5)

    # 商家資訊
    geogCoord_url = chrome.current_url.split(',')
    lat = geogCoord_url[0][-10:]  # 緯度
    lon = geogCoord_url[1]        # 經度

    time.sleep(3)
    # 餐廳名稱
    store_name = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]").text
    time.sleep(3)
    # 平均評價星等
    avg_rating = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span/span").text

    # 追加寫入 store_info.csv 檔
    # 記得改成自己存檔的位置
    filepath = r'/Users/yuchiaching/Desktop/googlemap_info.csv'

    with open(file=filepath, mode='a+', encoding='utf-8', newline='') as f1:

        writer = csv.writer(f1)

        tmp_list_1 = [store_name, lon, lat, avg_rating]
        writer.writerow(tmp_list_1)

    # 一些神奇的操作
    time.sleep(3)
    btn = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span/span[2]/span[1]/button")
    btn.click()
    time.sleep(3)
    btn = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[7]/div[2]/div/button")
    time.sleep(3)
    btn.click()
    time.sleep(3)
    trgt = chrome.find_element_by_id("action-menu").find_elements_by_tag_name("li")[1]
    ActionChains(chrome).double_click(trgt).perform()
    time.sleep(3)

    # 處理網址
    url_3 = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[4]/div[1]/ul/li[1]").get_attribute('ved')
    url_3 = url_3.split(':')[4]

    time.sleep(3)

    cur = "view-source:" + chrome.current_url
    chrome.get(cur)

    temp = chrome.find_element_by_xpath("/html/body/table/tbody/tr[155]/td[2]").text

    chrome.close()

    pos = temp.find('null,[\\"376')
    url_1 = temp[(pos + 8):(pos + 27)]
    pos = temp.find("ludocid\\\\u003")
    url_2 = temp[(pos + 14):(pos + 34)]
    url = ("https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y" + 
           url_1 + "!2y" + url_2 + "!2m2!1i0!2i10!3e2!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s" + url_3 + "!7e81")

    # 商家評論

    # 讀入連結
    tmp = url.split('1i0!')

    file_name = store_name[:6]

    # 建立商家評論檔案
    # 記得改成自己存檔的位置
    filepath = '/Users/yuchiaching/Desktop/' + file_name + '.csv'

    with open(file = filepath, mode='a+', encoding='utf-8', newline='') as f2:

        writer = csv.writer(f2)

        # 先試抓 100 則評論
        for i in range(0, 100, 10):

            # 根據連結結構，替換字串
            str_ = "1i" + str(i) + "!"    
            url_2 = str_.join(tmp)

            time.sleep(5)
            # 發送 get 請求
            text_2 = requests.get(url_2).text
            # 取代掉特殊字元，這個字元是為了資訊安全而設定
            pretext_2 = ')]}\''
            text_2 = text_2.replace(pretext_2,'')
            time.sleep(3)
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
