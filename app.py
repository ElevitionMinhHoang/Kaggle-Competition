import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))

st.title("Student Academic Warning Prediction")

st.write("Demo dự đoán cảnh báo học vụ")

age = st.slider("Age",17,30,20)
count_f = st.slider("Number of F subjects",0,10,1)
tuition = st.selectbox("Tuition Debt",[0,1])

if st.button("Predict"):

    X = np.array([[age,count_f,tuition]])

    pred = model.predict(X)

    if pred == 0:
        st.success("Normal")
    elif pred == 1:
        st.warning("Academic Warning")
    else:
        st.error("Dropout Risk")