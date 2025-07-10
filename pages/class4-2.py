import streamlit as st

st.title("🍽️點餐機")

if "order" not in st.session_state:
    st.session_state.order = []  # 新增一個購物車的list
col1, col2 = st.columns(2)
with col1:
    foodinput = st.text_input("請輸入餐點")
with col2:
    if st.button("加入", key="add"):
        st.session_state.order.append(foodinput)

st.write(f"### 🛒購物車")
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.order[i])
    with col2:
        if st.button("刪除", key=i):
            st.session_state.order.pop(i)
            st.rerun()
