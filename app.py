# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:38:32 2023

@author: debna
"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import ReLU
from tensorflow.keras.layers import Dropout
import numpy as np
import pickle
from pickle import load
import streamlit as st
import tensorflow as tf

df = load(open('E:/LiveProject/playground-series-s3e16_crab_age/crab_age.pickle', 'rb'))

st.title("Crabe Age Predictions")

Sex = st. radio("Select Crab Gender", ["M","F","I"])
if Sex == "M":
    Sex = 1
elif Sex == "I":
    Sex = 2
elif Sex == "F":
    Sex = 3

Length = st. number_input("Length", value = 0)
Diameter = st. number_input("Diameter", value = 0)
Height = st. number_input("Height", value = 0)
Weight = st. number_input("Weight", value = 0)
Shucked_Weight = st. number_input("Shucked Weight", value = 0)
Viscera_Weight = st. number_input("Viscera Weight", value = 0)
Shell_Weight = st. number_input("Shell Weight", value = 0)

if st. button("Predict"):
    query_point = np. array([Sex, Length, Diameter, Height, Weight, Shucked_Weight, Viscera_Weight, Shell_Weight])
    query_point = query_point. reshape(1, -1)
    prediction = df.predict(query_point)
    st.write("The predicted age is", prediction[0])














