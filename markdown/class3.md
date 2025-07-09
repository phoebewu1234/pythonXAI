## 🐍 Python 小學生入門筆記 ✨

### 🖨️ 基本輸出與輸入

#### `print()`：把東西顯示在螢幕上

```python
print("Hello!")  # 顯示 Hello!
```

#### `input()`：讓使用者輸入文字

```python
name = input("請輸入你的名字：")
print("你好，" + name)
```

> ❗ 不管輸入什麼，都是「字串」(文字)，像是 `"123"` 也是文字喔！

### 🔢 資料型態 type() 跟 轉換

#### 常見資料型態

- `int`：整數（例如 1）
- `float`：小數（例如 1.5）
- `str`：字串（例如 "apple"）
- `bool`：布林值（True 或 False）

#### 檢查資料型態

```python
print(type(1))  # int
print(type("apple"))  # str
```

#### 轉換資料型態

```python
int("10")     # 變成整數
float("3.14") # 變成小數
str(123)      # 變成文字
bool(1)       # 變成 True
```

### 🧮 運算子

#### 比較運算子

- `==` 相等
- `!=` 不相等
- `>` 大於
- `<` 小於
- `>=` 大於等於
- `<=` 小於等於

#### 邏輯運算子

- `and`：兩個都要對才會是 True
- `or`：只要有一個對就是 True
- `not`：相反的意思

#### 優先順序（從高到低）

1. 括號 `()`
2. 次方 `**`
3. 乘除 `* / // %`
4. 加減 `+ -`
5. 比較 `== != > <`
6. not
7. and
8. or

### 🔐 判斷式 if / elif / else

#### 讓程式做選擇

```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("再努力！")
```

> ⚠️ `elif` 是在前面條件不成立才會判斷，不會重複判斷。

### 🔁 迴圈 for

#### 重複做很多次

```python
for i in range(3):
    print("Hello!")
```

#### `range()` 說明

- `range(5)` → 0,1,2,3,4
- `range(1,5)` → 1,2,3,4
- `range(1,10,2)` → 1,3,5,7,9

### 💡 Streamlit 簡介（做網頁的工具）

- `st.write()`：顯示文字、數字
- `st.title()`：顯示大標題
- `st.button()`：做按鈕
- `st.balloons()`、`st.snow()`：加特效
- `st.number_input()`：輸入數字
- `st.success()`、`st.warning()`、`st.error()`：顯示不同提示

```python
import streamlit as st
st.title("我的第一個 Streamlit 網頁！")
```

### 🧱 List（清單）

#### 建立清單

```python
fruits = ["apple", "banana", "cherry"]
```

#### 常見操作

```python
print(fruits[0])  # apple
print(len(fruits))  # 幾個元素

fruits.append("orange")  # 加一個
fruits.remove("banana")  # 移除某個元素
fruits.pop()  # 移除最後一個
fruits.sort()  # 排序

for fruit in fruits:
    print(fruit)
```

#### 清單的拷貝

```python
a = [1, 2, 3]
b = a.copy()
b[0] = 99
print(a)  # 原本的不會變
```

### 📁 檔案操作

#### 打開檔案並讀取內容

```python
with open("檔案名稱.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

- `"r"`：讀取模式
- `"w"`：寫入模式（會蓋掉原本檔案）
- `"a"`：加在後面
- `with` 可以自動幫你關閉檔案

#### 判斷副檔名

```python
filename = "notes.md"
print(filename.endswith(".md"))  # 看是不是.md結尾
```

### 🔢 小挑戰：數字金字塔

```python
num = 5
for i in range(1, num + 1):
    print(str(i) * i)
```

➡️ 輸出：

```
1
22
333
4444
55555
```

---

📘 **小小總結：**

- Python 是一個可以讓我們和電腦「對話」的工具。
- 用簡單的指令就可以讓電腦幫我們做事情！
- 寫程式就像玩積木，動動腦、試試看，你也可以做出自己的小作品喔！
