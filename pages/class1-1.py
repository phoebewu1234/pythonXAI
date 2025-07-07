"""
多行註解
可以放很多文字
"""

# 單行註解
# Ctrl+? 可以快速註解/取消註解

# 基本型態
print(1)  # int整數，-1, 0, 1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9
print(1.0)  # float浮點數，-1.0, 0.0, 1.0 ,2.0 ,3.0 ,4.0 ,5.0 ,6.0 ,7.0 ,8.0
print(1.234)  # float浮點數
print("apple")  # str字串，"sadasd123125557","1"
print(True)  # bool布林值，True, False
print(False)  # bool布林值，True, False

# 變數
a = 10  # 新增一個儲存空間並取名為a，"="的功能是將右邊的值10存入左邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改為apple
print(a)  # 在終端機顯示a所存的值

# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 取商
print(1 % 1)  # 取餘數
print(2**3)  # 次方

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減

# 字串運算
print("apple" + "pen")  # 字串相加
print("apple" * 3)  # 字串乘法

# 練習
print("可以在終端機顯示文字")
print("之前學過的東西也可以印出來")
a = "hello"
b = "world"
print(a + " " + b)

# 字串格式化
name = "Apple"
age = 18
print(f"My name is {name}, I am {age} years old")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示
