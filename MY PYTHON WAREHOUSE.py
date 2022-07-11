import streamlit as st
from PIL import Image


st.title("MY PYTHON WAREHOUSE")
st.caption("覚えておきたいpythonのアルゴリズムコードを観覧したり、便利な数学計算がおこなえます。")

st.subheader("Who are you?")
image = Image.open("./data/profile.png")
st.image(image, width=100)
st.markdown("UC Berkeley出身の新米シリコンバレーエンジニアです。アメリカ語ﾁｮｯﾄﾜｶﾗﾅｲ。")
st.markdown("Twitter: [@Sorasukeprog](https://twitter.com/Sorasukeprog)")

st.subheader("How to Use")
st.text("サイドバーから各種アルゴリズムを観覧できます(詳しい解説はないのでご了承ください)。\nまた個人的にたまに使う数学計算のコードもまとめておきます。電卓代わりにご利用ください。\nコンテンツは作者の気まぐれで増えていくかもしれません。")