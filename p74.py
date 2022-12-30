# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:48:27 2022

@author: WIN-10
"""

# Necessary Libraries
import pickle
import streamlit as st
import numpy as np
import pandas as pd
import sklearn

st.title('Car Price Predictor')
cars24    = pickle.load(open('cars24dash.pkl','rb'))
model_DT  = pickle.load(open('model_DT.pkl','rb'))
#sidebar



   
def predict(Name, Model, Transmission, Kms, Owner, Fuel_Type,
            Registration, EMI, Year, Brand, State, Age):
   
   prediction = model_DT.predict(pd.DataFrame([[Name, Model, Transmission, Kms, Owner, Fuel_Type,
   Registration, EMI, Year, Brand, State, Age]],columns=['Name','Model','Transmission','Kms','Owner','Fuel_Type','Registration','EMI','Year','Brand','State','Age']))
   return prediction

    
col1,col2 = st.columns(2)
with col1:
   Brand=st.selectbox("Select the Brand Name",cars24['Brand'].unique())
   Name=st.selectbox("Select the Car Name",cars24["Name"].unique())
   Model=st.selectbox("Select the Car Model",cars24["Model"].unique())
   Transmission=st.selectbox("Select the Transmission Type",cars24["Transmission"].unique())
   Kms=st.number_input("Enter Kms")
   Owner=st.number_input("Enter Owner Number")
with col2:   
    Fuel_Type=st.selectbox("Select the Fuel Type",cars24["Fuel_Type"].unique())
    Registration=st.selectbox("Enter Registration Location",cars24['Registration'].unique())
    EMI=st.number_input("Enter EMI")
    Year=st.number_input("Enter the Year")
    State=st.selectbox("Enter the State",cars24['State'].unique())
    Age=st.number_input("Enter the Age")

   
if st.button("Predict"):
     price = predict(Name, Model, Transmission, Kms, Owner, Fuel_Type,
     Registration, EMI, Year, Brand, State, Age)
     st.success(f'The Predicted Price of car is  ₹  {price[0]:.2f}')
       
      