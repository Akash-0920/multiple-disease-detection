# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:35:03 2022

@author: Akash
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
diabetes_model=pickle.load(open(r"C:/Users/Akash/Desktop/multiple disease/diabetes.sav",'rb'))
heart_disease_model=pickle.load(open(r"C:/Users/Akash/Desktop/multiple disease/heart_disease.sav",'rb'))
parkinson_model=pickle.load(open(r"C:/Users/Akash/Desktop/multiple disease/parkinsons_model.sav",'rb'))



#side bar for navigation
with st.sidebar:
    
    selected=option_menu("Multiple Disease Predictive system",
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinson disease Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)

#Diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    #page  title
    st.title('Diabetes Prediction Using ML')
    
    
    #getting the input data from the user
    #column for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose=st.text_input("Glucose level")
    with col3:
        BloodPressure = st.text_input("Bllood Pressure value")
    with col1:
        SkinThickness = st.text_input("Skin thickness value")
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        Diabetespredigreefunction = st.text_input('Diabetes pedigree function value')
    with col2:
        Age=st.text_input('Age of person')
    
   
    
    


    #code for prediction
    diab_diagnosis=''
    
    #creating button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,Diabetespredigreefunction,Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis= 'The Person is Diabetic'
        elif(diab_diagnosis[0]==0):
            diab_diagnosis='The Person is not Diabetic'
    st.success(diab_diagnosis)
#heart disease prediction
if (selected=='Heart disease Prediction'):
    # page title
    st.title('Heart disease Prediction Using ML')

    
#Parkinson Disease
if (selected=='Parkinson disease Prediction'):
    #page title
    st.title('Parkinson Disease Prediction using ML')


