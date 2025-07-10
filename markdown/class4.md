## 🐍 今天我們學了什麼 Python？

### 🌟 Streamlit 小工具

#### 1️⃣ 建立標題

```python
st.title("我的標題")
```

會在畫面上顯示大大的字！

---

#### 2️⃣ 建立欄位（columns）

我們可以把畫面切成幾個區塊，像這樣：

```python
col1, col2 = st.columns(2)  # 分成兩欄
```

你也可以指定比例：

```python
col1, col2 = st.columns([1, 2])  # col1小一點、col2大一點
```

還可以用 `for` 迴圈產生很多欄：

```python
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

---

#### 3️⃣ 按鈕

```python
st.button("點我一下", key="按鈕的名字")
```

每個按鈕要有自己的 `key`，不然會搞混。

---

#### 4️⃣ 文字輸入框

```python
st.text_input("請輸入內容", value="預設的文字")
```

可以讓使用者輸入一些字。

---

#### 5️⃣ 🎈 氣球效果

```python
st.balloons()
```

當我們做對事情時，可以放氣球慶祝一下！

---

#### 6️⃣ 分隔線

```python
st.write("---")
```

讓畫面更整齊漂亮。

---

### 🛍️ 製作購物車（點餐機）

```python
if "order" not in st.session_state:
    st.session_state.order = []  # 建立空的購物車

food = st.text_input("輸入你要點的餐點")

if st.button("加入"):
    st.session_state.order.append(food)  # 把餐點加進去

for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.order[i])  # 顯示每個餐點
    with col2:
        if st.button("刪除", key=i):  # 如果按下刪除
            st.session_state.order.pop(i)  # 從購物車拿掉
            st.rerun()  # 重新整理畫面
```

---

### 🧠 什麼是 `st.session_state`？

這是 **Streamlit 幫我們記住東西的地方**。

當你按下按鈕或做其他事，它會記住你之前的結果，就不會忘記！

---

### ➕ 算術指定運算子

這些可以快速做加減乘除！

| 指令      | 意思      |
| --------- | --------- |
| `a += 1`  | a = a + 1 |
| `a -= 1`  | a = a - 1 |
| `a *= 2`  | a = a × 2 |
| `a /= 2`  | a = a ÷ 2 |
| `a //= 2` | 整數除法  |
| `a %= 2`  | 餘數      |
| `a **= 2` | 次方      |

---

### 🔁 while 迴圈（重複做事情）

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

它會一直做，直到條件不成立。

---

### 🔂 break 可以強制跳出迴圈

```python
while True:
    if something:
        break  # 馬上跳出去！
```

---

### 🎲 隨機數字（抽籤遊戲）

```python
import random
ans = random.randint(1, 100)  # 1到100之間的數字
```

這可以用來做猜數字的遊戲！

---

### 📖 字典 Dictionary（像是資料小字典）

```python
d = {"apple": 20, "banana": 30}
```

- `d["apple"]` 會拿到 20。
- `d["banana"] = 25` 可以修改。
- `d["orange"] = 15` 可以新增。

---

#### 遍歷字典的 4 種方法：

```python
for k in d:           # 拿到key
for k in d.keys():    # 拿到key
for v in d.values():  # 拿到value
for k, v in d.items():  # 同時拿到key和value
```

---

#### 刪除字典的資料

```python
d.pop("apple")
```

也可以這樣防止錯誤：

```python
d.pop("notfound", "沒有這筆資料")
```

---

### 🎉 太棒了！

今天我們學到了超多 Python 的基礎知識，也做了一個點餐機！
只要慢慢學，一定會變成 Python 小高手！🚀
