import streamlit as st
from PIL import Image

st.title("みっふぃーさんサンプル材料")

image0 = Image.open('0.png')
image1 = Image.open('1.png')
image2 = Image.open('2.png')
image3 = Image.open("3.png")
image4 = Image.open("4.png")
image5 = Image.open("5.png")
image6 = Image.open("6.png")

st.image(image0, caption="星情報")
st.image(image1, caption="活動バイオリズム情報")
st.image(image2, caption="コートカードと属性情報")
st.image(image3, caption="読み位置情報")
st.image(image4, caption="イヤーカード/ソウルカード")
st.image(image5, caption="CUBE/グラフ")
st.image(image6, caption="CUBE/BOX<健在意識/潜在意識>")