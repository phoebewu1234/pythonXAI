# len：取得字典中有多少組 key-value 配對
d = {"apple": 20, "banana": 30, "orange": 25}
print(len(d))  # 3，字典中有三組 key-value 配對

# 檢查某個 key 是否存在於字典中
# 使用前先檢查可以避免 KeyError 錯誤
d = {"apple": 20, "banana": 30, "orange": 25}
print("apple" in d)  # True, apple 這個 key 存在
print("wax apple" in d)  # False, wax apple 這個 key 不存在

# 檢查某個元素有沒有在list中
# 使用 in 可以快速檢查某個元素是否存在於list中
L = [1, 2, 3, 4, 5]
print(3 in L)  # True, 3 在 List 中

# 比較複雜的dick
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1, 2, 3]
print(d["a"][0])  # 1
print(d["b"])  # ['c': 4, 'd': 5]
print(d["b"]["c"])  # 4

# 成績登記系統，key是學生名字，value是學生成績，每個科目有3個成績
grade = {
    "小明": {"國文": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 75]},
    "小美": {"國文": [88, 78, 68], "數學": [83, 73, 63], "英文": [93, 83, 73]},
    "小華": {"國文": [86, 76, 66], "數學": [81, 71, 61], "英文": [91, 81, 71]},
}

# 取得小明的數學成績
print(grade["小明"]["數學"])  # [85, 75, 65]
# 取得小美的第一次英文成績
print(grade["小美"]["英文"][0])  # 93
# 取得小華的第二次國文成績
print(grade["小華"]["國文"][1])  # 76
