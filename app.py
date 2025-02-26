import streamlit as st
from ultralytics import YOLO
import pandas as pd
import numpy as np
from io import StringIO
import PIL
from PIL import Image
import requests
from io import BytesIO

brain_cancer_model = r"models\brain_detect.pt"
skin_cancer_model = "models\skin_detect.pt"

st.set_page_config(page_icon=":brain", page_title="Cancer Detection", layout="wide")

st.title("Cancer Detection")
st.text("Upload image here:")

with st.sidebar:
    with st.expander("Dataset Links", expanded= True):
        st.markdown("[Brain Cancer Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)")
        st.markdown("[Skin Cancer Dataset](https://www.kaggle.com/datasets/nodoubttome/skin-cancer9-classesisic)")


uploaded_file = st.file_uploader("Choose a file", type=['png', 'jpg'])
if uploaded_file is not None:
    

    st.write("filename:", uploaded_file.name)
    uploaded_image = PIL.Image.open(uploaded_file)
    st.image(uploaded_image, caption='Input', width=300)

    st.divider()

    type_=st.selectbox("Choose any one type of detection", (('Brain'), ('Skin')))
    conf = st.slider('Set confidence level percentage', 0, 100, 25)
    
    if st.button("Detect cancer"):
        with st.spinner("Detecting Cancer"):
            if type_=='Brain':
                model= YOLO(brain_cancer_model)
                confi=conf/100
                res=model(uploaded_image, conf=confi)
                img=res[0].plot()
                a=res[0]
                if a.masks is not None:
                    st.image(img, caption='Output', width=500)
                else:
                    st.write("No detections found")

            if type_=='Skin':                
                model= YOLO(skin_cancer_model)
                confi=conf/100
                res=model(uploaded_image, conf=confi)
                img=res[0].plot()
                a=res[0]
                if a.masks is not None:
                    st.image(img, caption='Output', width=500)
                else:
                    st.write("No detections found")
    
