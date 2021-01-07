# coding: utf-8

# 引入函式庫
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import requests
import json
import csv
import time
import re
import random

name_list = list()

# 讀出商家清單
# 記得改成自己放檔案的位置
with open(file='/Users/yuchiaching/Desktop/GitHub/PBC_Final/store_info.csv', mode='r', encoding='utf-8', newline='') as f:

    rows = csv.reader(f)

  # 以迴圈輸出每一列
    for row in rows:
        full_name = row[0] + " 台大"
        name_list.append(full_name)

for i in range(len(name_list)):

    # 主要用途為取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。
    options = Options()
    options.add_argument("--disable-notifications")
    # 在背景運作
    # options.add_argument("--headless")
    # 無痕模式
    options.add_argument("--incognito")

    proxies = {
        "http" : "http://139.180.142.243:3128",
        "http" : "http://111.155.124.78:8123", # 代理ip
        "http" : "http://198.211.100.174:3128",
        "http" : 'http://96.9.211.200:80'
    }
   
    headers = {
        "User_Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    }


    # 取用 chromedriver
    # 記得改 chromedriver 的位置
    chrome = webdriver.Chrome('/Users/yuchiaching/Desktop/GitHub/PBC_Final/chromedriver', chrome_options=options)
    chrome.maximize_window()
    time.sleep(5)
    chrome.get("https://www.google.com.tw/maps")
    time.sleep(5)
    searchbox_input = chrome.find_element_by_id("searchboxinput")
    time.sleep(2)
    searchbox_input.send_keys(name_list[i])
    time.sleep(2)
    searchbox_input.send_keys(Keys.ENTER)
    time.sleep(5)

    商家資訊
    geogCoord_url = chrome.current_url.split(',')
    lat = geogCoord_url[0][-10:]  # 緯度
    lon = geogCoord_url[1]        # 經度
    time.sleep(3)

    # 餐廳名稱
    time.sleep(3)
    store_name = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]").text
    time.sleep(3)
    # 評論數
    comment_cnt = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span/span[2]/span[1]/button").text
    comment_cnt = comment_cnt.split(' ')
    comment_cnt = comment_cnt[0].split(',')
    comment_cnt = ''.join(comment_cnt)
    time.sleep(3)
    # 平均評價星等
    avg_rating = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div[2]/span/span/span").text
    time.sleep(3)

    # 追加寫入 store_info_final.csv 檔
    filepath = r'/Users/yuchiaching/Desktop/GitHub/PBC_Final/store_info_final.csv'

    with open(file=filepath, mode='a+', encoding='utf-8', newline='') as f1:

        writer = csv.writer(f1)

        tmp_list_1 = [store_name, lon, lat, comment_cnt, avg_rating]
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

    # 獲取網址片段三
    url_3 = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[4]/div[1]/ul/li[1]").get_attribute('ved')
    url_3 = url_3.split(':')[4]
    print(url_3)
    
    time.sleep(3)

    cur = "view-source:" + chrome.current_url
    chrome.get(cur)

    temp = chrome.find_element_by_xpath("/html/body/table/tbody/tr[155]/td[2]").text

    # 獲取網址片段一
    pos = temp.find('null,[\\"376')
    url_1 = temp[(pos + 8):(pos + 27)]
    # 獲取網址片段二
    pos = temp.find("ludocid\\\\u003d")
    url_2 = temp[(pos + 14):(pos + 34)]
    url_2 = list(url_2)
    curr_url_2 = list()
    for i in url_2:
        if i.isdigit() is True:
            curr_url_2.append(i)
    url_2 = "".join(curr_url_2)

    # 組成完整網址
    url = ("https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y" + 
           url_1 + "!2y" + url_2 + "!2m2!1i0!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s" + url_3 + "!7e81")

    # 商家評論

    # 讀入連結
    tmp = url.split('1i0!')

    # 建立商家評論檔案
    # 記得改成自己存檔的位置
    filepath = '/Users/yuchiaching/Desktop/GitHub/PBC_Final/google_map_comment.csv'

    with open(file = filepath, mode='a+', encoding='utf-8', newline='') as f2:

        writer = csv.writer(f2)

        print(comment_cnt)

        cnt = 0

        if (int(comment_cnt) >= 500) or comment_cnt == '':
            cnt = 500
        else:
            cnt = int(comment_cnt)

        for i in range(0, cnt, 10):

            # 根據連結結構，替換字串
            print(i)
            str_ = "1i" + str(i) + "!"    
            url_all = str_.join(tmp)
            print(url_all)

            text_2 = requests.get(url=url_all, headers=headers, proxies=proxies, timeout=30).text
            time.sleep(5)
            # 取代掉特殊字元，這個字元是為了資訊安全而設定
            pretext_2 = ')]}\''
            text_2 = text_2.replace(pretext_2,'')
            # 把字串讀取成 json
            soup = json.loads(text_2)
            conlist = soup[2]

            for j in conlist:

                # 用戶名
                username = str(j[0][1])
                # 評論時間
                comment_time = str(j[1])
                # 評價星等
                rating = str(j[4])
                # 評價內容（刪除換行符號)
                comment = str(j[3])
                comment = re.sub(r",", "，", comment)
                comment = comment.replace('\n', ' ')

                tmp_list_2 = [store_name,username, comment_time, rating, comment]
                writer.writerow(tmp_list_2)

    print("\n" + str(store_name) + "\nFINISH!\n")

    chrome.close()
