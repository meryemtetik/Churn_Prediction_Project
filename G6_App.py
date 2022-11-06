from re import M
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Employee Churn Prediction",
    )

st.markdown("<h1 style='text-align: center; color: Indigo;'>Employee Churn Prediction Application</h1>", unsafe_allow_html=True)

_, col2, _ = st.columns([2.3, 3, 2])

#with col2:  
    #img = Image.open("churn.jpg")
    #st.image(img, width=320)

img = Image.open("churn1.png")
st.image(img,caption="cattie")

st.success('###### The model was trained with the following parameters of nearly 15000 employees.')


st.info("###### 1. Satisfaction level: Employee satisfaction point, which ranges from 0-100 :smiley:\n"
         "###### 2. Performance: Evaluated performance, which also ranges from 0-100 :male-detective:\n"
         "###### 2. Performance: Evaluated performance, which also ranges from 0-100 :male-detective:\n"
         "###### 3. Working years: The number of years spent by an employee in the company :older_adult:\n"
         "###### 4. Working hours: How many hours an employee worked in a month? :stopwatch:\n"
         "###### 5. Number of projects: How many projects the employee is assigned to? :open_file_folder:\n"
         "###### 6. Work accident: Whether an employee has had a work accident or not :face_with_head_bandage:\n"
         "###### 7. Promotion: Has the employee  had a promotion in the last 5 years :gift:\n"
         "###### 8. Departments: Employee's working department/division :female-mechanic:\n"
         "###### 9. Salary: Salary level of the employee; low, medium and high :moneybag:\n"
         "###### 10. Left: Whether the employee has left the company or not :slightly_frowning_face:")

st.success("###### Please enter the information of the employee for prediction from the left side bar and below")

import pickle
filename = 'model_xgb_tuned.pkl'
model = pickle.load(open(filename, 'rb'))


col, col2 = st.columns([4, 4])
with col:
    st.markdown("###### Please select a department")
    Department = st.selectbox("Departments",
            ('sales', 'accounting', 'hr', 'technical', 'support', 'management',
        'IT', 'product_mng', 'marketing', 'RandD')
        )
with col2:
    st.markdown("###### Please select a salary")
    Salary = st.radio(
        "Salary",
        ('low', 'medium', 'high')
        )
    if Salary == "low":   
         Salary = 0 
    elif Salary == "medium":
         Salary = 1
    elif Salary == "high":
         Salary = 2

col1, col2 = st.columns([4, 4])

with col1:
    st.markdown("#####")
    st.markdown("###### Has the employee ever had a work accident?")
    Work_accident = st.radio(
        "Accident",
        ('No', 'Yes')
        )   

    if Work_accident == "Yes":   
        Work_accident = 1 
    elif Work_accident == "No":     
        Work_accident = 0
        
with col2:
    st.markdown("#####")
    st.markdown("###### Received any promotions in the past five years?")   
    promotion_last_5years = st.radio(
        "Promotion",
        ('Yes', 'No')
        )   
if promotion_last_5years == "Yes":   
    promotion_last_5years = 1 
elif promotion_last_5years == "No":     
    promotion_last_5years = 0


satisfaction_level = st.sidebar.slider("Satisfaction level:",min_value=9, max_value=100)

last_evaluation = st.sidebar.slider("Performance:",min_value=36, max_value=100)

time_spend_company = st.sidebar.slider("Working years:",min_value=2, max_value=10)

average_montly_hours = st.sidebar.slider("Working hours:",min_value=96, max_value=310)

number_project = st.sidebar.slider("Number of projects:",min_value=2, max_value=7)



   
my_dict = {
    'departments': Department,
    'salary': Salary,
    'satisfaction_level': (satisfaction_level/100) ,
    'last_evaluation': last_evaluation/100,
    'number_project': number_project,
    'average_montly_hours': average_montly_hours,
    'time_spend_company': time_spend_company,
    'Work_accident': Work_accident,
    'promotion_last_5years': promotion_last_5years  
}


df=pd.DataFrame.from_dict([my_dict])

col, col2 = st.columns([4, 4])

with col: 
    st.info("The Predictors for Your Employee")
    my_dict


with col2: 
    if st.button("Predict"):
        pred = model.predict(df)
        if int(pred[0]) == 1:
            st.error("Your employee is very likely to leave the company")
        else:
            st.success("Your employee is loyal to the company")