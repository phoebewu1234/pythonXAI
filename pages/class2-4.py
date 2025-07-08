import streamlit as st

# st.number_input()可以讓使用者輸入數字，可以進行以下設定：
# step=1可以讓使用者只能輸入整數
# min_value=0，可以設定最小值為0
# max_value=100，可以設定最大值為100
number = st.number_input("請輸入一個數字：", step=1, min_value=0, max_value=100)
# 顯示使用者輸入的數字
st.write(f"你輸入的數字是：{number}")

st.write("---")

st.write("## 練習")
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
