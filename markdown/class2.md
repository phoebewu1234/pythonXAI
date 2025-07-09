# 🐍《超簡單 Python 小學生筆記》

---

## 🟦 1. `print()`：讓電腦說話

```python
print("Hello!")  # 顯示 Hello!
```

就像跟電腦說：「幫我說這句話～」

---

## 🟦 2. `len()`：算字的長度

```python
print(len("apple"))  # ➜ 5
print(len(","))      # ➜ 1
```

`len()` 就是幫你數有幾個字。

---

## 🟦 3. `type()`：看資料是什麼型態

```python
print(type(1))        # 整數 int
print(type(1.0))      # 小數 float
print(type("apple"))  # 字串 str
print(type(True))     # 布林值 bool
```

就像幫東西貼上標籤：「這是數字、這是字、這是真的或假的」

---

## 🟦 4. 型態轉換（把東西換成另一種）

```python
print(int(1.0))      # 小數變整數
print(float(1))      # 整數變小數
print(str(1))        # 整數變字
print(bool(1))       # 整數變真假
print(float("1.234"))# 字變小數
print(str(1.234))    # 小數變字
```

🔴 錯誤例子（不能把「hello」變數字）：

```python
# print(int("hello"))  # ❌會報錯！
```

---

## 🟦 5. `input()`：讓使用者輸入東西

```python
a = input("請輸入一些文字：")
print(int(a) + 10)
```

🧠 輸入的東西，會變成字串（就是文字），如果要當數字用，要先轉型！

---

## 🟦 6. 計算圓面積的小練習

```python
pi = 3.14
r = float(input("請輸入圓的半徑："))
area = pi * r * r
print(f"圓的面積為：{area}")
```

📌 這裡我們用 `f-string`，讓我們可以把變數塞進句子裡～

---

## 🟦 7. Streamlit：畫面漂亮的 Python 工具 ✨

（這是給大人或老師看的畫面）

```python
import streamlit as st

st.title("這是標題")
st.write("可以顯示文字、數字，還能用 Markdown 排版")
st.markdown("* **粗體**\n* *斜體*")
```

也能做：

```python
st.info("這是資訊")
st.success("成功囉！")
st.warning("小心喔～")
st.error("錯誤了 QQ")
```

---

## 🟦 8. 比較運算子（比大小）

```python
print(1 == 1)  # 相等 ➜ True
print(1 != 1)  # 不等於 ➜ False
print(1 > 0)   # 大於
print(1 < 2)   # 小於
print(2 >= 2)  # 大於等於
print(2 <= 3)  # 小於等於
```

---

## 🟦 9. 邏輯運算子（而且、或者、不）

```python
print(True and False)  # 兩個都要是 True 才是 True
print(True or False)   # 只要一個是 True 就是 True
print(not True)        # 相反意思
```

🧠 小提醒：先算括號、再算 not，再 and，最後才 or！

---

## 🟦 10. 判斷式 `if`：密碼小遊戲

```python
password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確！")
elif password == "000000":
    print("密碼正確！")
else:
    print("密碼錯誤！")
```

📌 可以用 `if...elif...else` 讓電腦做選擇！

---

## 🟦 11. Streamlit 練習：顯示成績等級

```python
number = st.number_input("請輸入你的分數：", step=1, min_value=0, max_value=100)
if number >= 90:
    st.write("A")
elif number >= 80:
    st.write("B")
elif number >= 70:
    st.write("C")
elif number >= 60:
    st.write("D")
else:
    st.write("E")
```

📌 根據使用者輸入的成績，自動顯示等級！

---

## 🎉 你學會了這些：

✅ 顯示文字 `print()`
✅ 數字與文字的型態與轉換
✅ 使用者輸入 `input()`
✅ f-string 變魔法文字
✅ if 判斷式
✅ Streamlit 建立漂亮網頁介面
✅ 做成小遊戲／成績顯示器 🎮
