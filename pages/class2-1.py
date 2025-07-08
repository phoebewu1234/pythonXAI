print(len("apple"))  # len()函數可以取得字串的長度
print(len(","))  # len()函數可以取得字串的長度
# type()  # 可以查看變數的型態
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

# 型態轉換
print(int(1.0))  # float轉int
print(float(1))  # int轉float
print(str(1))  # int轉str
print(bool(1))  # int轉bool
print(int(1.234))  # float轉int
print(float("1.234"))  # str轉float
print(str(1.234))  # float轉str
print(bool(1.234))  # float轉bool
# print(int("hello"))  # 這行會報錯，因為字串中如果有非數字的字元，無法轉換成數字

# input()函式的使用
print("輸入開始")
# input()是一個函式，可以讓使用者輸入文字
# ()裡面的文字式提式訊息會先顯示在終端機才會等待使用者輸入
a = input("請輸入一些文字：")
print("輸入結束")
print(int(a) + 10)
print(type(a))  # 證明透過input()輸入內容都是字串

pi = 3.14
r = input("請輸入一個數字：")
Area = pi * (int(r) ** 2)
print(Area)

# 計算圓面積
# 這裡的input()會讓使用者輸入半徑，並轉成float型態
r = float(input("請輸入圓的半徑："))
area = 3.14 * r * r  # 計算圓的面積
print(f"圓的面積為：{area}")  # 使用f-string格式化輸出結果
