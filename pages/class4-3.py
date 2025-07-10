# 算術指定運算子
a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0
a //= 2  # a = a // 2
print(a)  # 0
a %= 2  # a = a % 2
print(a)  # 0.0
a **= 2  # a = a ** 2
print(a)  # 0.0

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or
# 9. += -= *= /= //= %= **= 算術指定運算子

# while 迴圈
# while 會搭配一個條件來使用
# 條件式為 True 時會一直執行迴圈
# 條件式為 False 時會跳出迴圈
# 每次迴圈執行完成完都會重新檢查條件有沒有變成 False
i = 0
while i < 5:
    print(i)
    i += 1  # i = i + 1

# break 可以強制跳出迴圈
# 先判斷break屬於哪個迴圈，然後跳出該迴圈
i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
    if i == 3:
        break  # 跳出迴圈，屬於while迴圈
    i += 1

for i in range(5):
    print(i)
    if i == 3:
        break  # 跳出迴圈

import random  # 匯入ramdom模組

# random.randrange()設定抽籤範圍方式一定要設定開始與結束
print(random.randrange(7))  # 0~6
print(random.randrange(1, 7))  # 1~6
print(random.randrange(1, 7, 2))  # 1~6，間隔2

# random.randint()設定抽籤範圍方式一定要設定開始與結束
# 且結束的數字會包含在內
print(random.randint(1, 6))  # 1~6

ans = random.randint(1, 100)  # 隨機產生1~100的整數
while True:  # 無窮迴圈
    num = int(input(f"請輸入1到100的整數："))  # 輸入數字

    if num < 0 or num > 100:  # 如果輸入的數字不在1~100之間
        print("請輸入1到100的整數")
    elif num > ans:  # 如果輸入的數字大於答案
        print("太大了！")
    elif num < ans:  # 如果輸入的數字小於答案
        print("太小了！")
    else:  # 如果輸入的數字等於答案
        print("答對了！")
        break  # 跳出迴圈

# 字典(Dictionary): 用來儲存[key, value] 配對的資料結構
# 字典很適合用來表示有對應關係的資料，像是商品和價格的對應

# 建立字典: 使用大括號{}，key和value之間用冒號: 分隔
d = {"apple": 20, "banana": 30, "orange": 25}
print(d)

# 從字典中取得特定 key 對應的 value
# 如果 key 不存在會產生 KeyError 錯誤
d = {"apple": 20, "banana": 30, "orange": 25}
print(d["apple"])
# print(d["pear"])  # 這行會產生 KeyError: 'pear' 錯誤

# 遍歷字典：有多種方式可以走訪字典中的資料
d = {"apple": 20, "banana": 30, "orange": 25}

# 方法一：直接遍歷字典，會取得所有的 key
for k in d:
    print(k)  # 印出 key 名稱
    print(d[k])  # 用 key 對應的 value

# 方法二：明確使用 keys() 方法來取得所有 key
for k in d.keys():
    print(k)  # 印出 key 名稱
    print(d[k])  # 用 key 來取得對應的 value

# 方法三：使用 values() 方法來取得所有 value
for v in d.values():
    print(v)  # 直接印出 value，但不知道對應的 key是什麼

# 方法四：使用 items() 方法同時取得 key 和 value
# 這是最常用的方法，因為可以同時存取 key 和 value
for k, v in d.items():
    print(f"{k}: {v}")  # 同時印出 key 和 value 的配對關係

# 新增/修改字典的內容
# 直接指定 key 對應的 value，如果 key 已存在就是修改，如果 key 不存在則是新增
d = {"apple": 20, "banana": 30, "orange": 25}
d["apple"] = 10  # 修改「apple」對應的 value
print(d)
d["wax apple"] = 15  # 新增一個 key-value 配對
print(d)

# 刪除字典的內容
d = {"apple": 20, "banana": 30, "orange": 25}
d.pop("apple")  # 刪除apple
# 如果要刪除的key不存在，會出現KeyError
# 這時候可以加上第二個參數，當key不存在時，不會有任何變化
popitem = d.pop("wax apple", "不存在這筆資料")  # 不會有任何變化
print(d)  # {'banana': 30, 'orange': 25}
print(popitem)  # 不存在這筆資料
