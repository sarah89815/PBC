# coding: utf-8

# 引入函式庫
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pyautogui
import requests
from fake_useragent import UserAgent
import json
import csv
import time

name_list = list()

# 讀出商家清單
# 記得改成自己放檔案的位置
with open(file='C:\\Users\\JasonChen\\Desktop\\github\\self_only\\store_info_5.csv', mode='r', encoding='utf-8', newline='') as f:

    rows = csv.reader(f)

  # 以迴圈輸出每一列
    for row in rows:
        name_list.append(row[0])

for store in name_list:

    # 主要用途為取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。
    options = Options()
    options.add_argument("--disable-notifications")
    # 在背景運作
    options.add_argument("--headless")
    # 改換useragent
    ua = UserAgent()
    ub = ua.random
    options.add_argument(f'user-agent={ub}')

    # 取用 chromedriver
    # 記得改 chromedriver 的位置
    chrome = webdriver.Chrome('C:\\Users\\JasonChen\\Desktop\\github\\self_only\\chromedriver', chrome_options=options)
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

    # 一些神奇的操作
    time.sleep(3)
    btn = chrome.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[7]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span/span[2]/span[1]/button")
    btn.click()
    time.sleep(3)
    # google自己的關鍵字(word)和提到幾次(figure)
    word1 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[2]/div/button/span[1]").text
    word2 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[3]/div/button/span[1]").text
    word3 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[4]/div/button/span[1]").text
    word4 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[5]/div/button/span[1]").text
    word5 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[6]/div/button/span[1]").text
    word6 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[7]/div/button/span[1]").text
    word7 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[8]/div/button/span[1]").text
    word8 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[9]/div/button/span[1]").text
    word9 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[10]/div/button/span[1]").text
    word10 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[11]/div/button/span[1]").text
    fig1 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[2]/div/button/span[2]").text
    fig2 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[3]/div/button/span[2]").text
    fig3 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[4]/div/button/span[2]").text
    fig4 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[5]/div/button/span[2]").text
    fig5 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[6]/div/button/span[2]").text
    fig6 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[7]/div/button/span[2]").text
    fig7 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[8]/div/button/span[2]").text
    fig8 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[9]/div/button/span[2]").text
    fig9 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[10]/div/button/span[2]").text
    fig10 = chrome.find_element_by_xpath("//*[@id='pane']/div/div[1]/div/div/div[2]/div[8]/div[11]/div/button/span[2]").text
    chrome.close()
    
    # 追加寫入 store_info.csv 檔
    # 記得改成自己存檔的位置
    filepath = r'C:\Users\JasonChen\Desktop\github\self_only\googlemap_info.csv'

    with open(file=filepath, mode='a+', encoding='utf-8', newline='') as f1:

        writer = csv.writer(f1)

        tmp_list_1 = [store_name, lon, lat, avg_rating]
        tmp_list_2 = [word1, fig1, word2, fig2, word3, fig3, word4, fig4, word5, fig5, word6, fig6, word7, fig7, word8, fig8, word9, fig9, word10, fig10]
        writer.writerow(tmp_list_1)
        writer.writerow(tmp_list_2)
    print("\n" + str(store_name) + "\nFINISH!\n")