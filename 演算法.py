import csv

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
filepath = r'/Users/yuchiaching/Desktop/GitHub/PBC_Final/store_info_final.csv'

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
def filter(store_list, keywords_list):
    # 新增一個空清單

    done = list()

    for keyword in keywords_list:
        # 檢查每一間商家是否符合條件，符合條件的加入 done 清單
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

    # 回傳過濾後的商家清單
    return done


# 定義選擇價格區間
# 傳入待過濾的 商家清單 以及 價格上界
def price_choose(store_list, upperbound):
    # 新增一個空清單
    done = list()

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

    # 回傳過濾後的商家清單
    return done


# 定義選擇評價區間
# 傳入待過濾的 商家清單 以及 評價下界
def ranking_choose(store_list, lowerbound):
    # 新增一個空清單
    done = list()

    # 轉成浮點數
    lowerbound = float(lowerbound)

    # 檢查每一間商家是否符合條件，符合條件的加入 done 清單
    for store in store_list:
        if store.avg_ranking >= lowerbound:
            done.append(store)

    # 回傳過濾後的商家清單
    return done


# check
# all_type = list()

# for store in stores:
#     for types in store.types:
#         all_type.append(types)
# print(set(all_type))

# 測試
print('測試關鍵字，請輸入關鍵字，可輸入多個以半形空白分割')
keyword = input()

keyword = keyword.split()

result = filter(stores, keyword)

for store in result:
    print(store)

print('測試價格區間，請輸入價格上限')
price = input()
result_price = price_choose(result, price)

for store in result_price:
    print(store)

print('測試評價區間，請輸入評價下限')
ranking = input()
result_ranking = ranking_choose(result_price, ranking)

for store in result_ranking:
    print(store)
