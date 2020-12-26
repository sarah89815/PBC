import csv

# 建立商家 class
class Store:
    def __init__(self, name, lowerbound, upperbound, area, types):
        self.name = name                   # 名稱
        self.lowerbound = int(lowerbound)  # 價錢區間下界
        self.upperbound = int(upperbound)  # 價錢區間上界
        self.area = area                   # 區域
        self.types = types                 # 種類 (是一個清單)

    def __str__(self):
        return str(self.name)


# 所有商家清單
stores = list()
# 商家關鍵字清單
store_keywords = list()

# 記得改成存檔案的地方
filepath = r'/Users/yuchiaching/Desktop/GitHub/PBC_Final/store_info_final.csv'

with open(file=filepath, mode='r', encoding='utf-8', newline='') as csvfile:
    rows = csv.reader(csvfile)

    rows_cnt = 0
    for row in rows:

        if rows_cnt % 2 == 0:
            # 將價格區間切分為上界和下界儲存
            price_intl = row[4].split('-')

            # 轉成 store 類別存入 stores 清單
            stores.append(Store(row[0], price_intl[0], price_intl[1], row[5], row[6:len(row)]))
        else:
            store_keywords.append(row)

        rows_cnt += 1

# 定義過濾函式
# 傳入待過濾的商家清單以及關鍵字
def filter(store_list, keyword):
    # 新增一個空清單
    done = list()

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

    # 回傳過濾後的商家清單
    return done


# 定義選擇價格區間
# 傳入待過濾的商家清單以及價格上界
def price_choose(store_list, upperbound):
    # 新增一個空清單
    done = list()

    # 轉成整數
    upperbound = int(upperbound)

    # 檢查每一間商家是否符合條件，符合條件的加入 done 清單
    for store in store_list:
        # 如果指定上界在
        if store.upperbound <= upperbound:
            done.append(store)
        elif (store.upperbound > upperbound) and (store.lowerbound < upperbound):
            done.append(store)
        else:
            continue

    # 回傳過濾後的商家清單
    return done


# check
# all_type = list()

# for store in stores:
#     for types in store.types:
#         all_type.append(types)
# print(set(all_type))

# 測試
print('測試關鍵字，請輸入關鍵字')
keyword = input()

result = filter(stores, keyword)

for store in result:
    print(store)

print('測試價格區間，請輸入價格上限')
price = input()
result_price = price_choose(result, price)

for store in result_price:
    print(store)
