# 比較運算子
print(1 == 1)  # True
print(1 != 1)  # False
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True

# # 邏輯運算子
# # and 運算子，只要有一個條件為 False，結果就是 False
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or 運算子，只要有一個條件為 True，結果就是 True
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not 運算子
print(not True)  # False
print(not False)  # True

# 優先順序
# 1. ()括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5. == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or

# 密碼門檢查
password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確！")
elif password == "654321":
    print("密碼正確！")
elif password == "000000":
    print("密碼正確！")
else:  # 沒有達成上面條件就會執行以下內容
    print("密碼錯誤！")
