import streamlit as st
import datetime
import os
import pandas as pd
import numpy as np
import pickle

class DataCleaning:

  def MapTransform(self,df):
    # Taking Log transform of Annual income
    df['Annual Income']=np.log(df['Annual Income'])

    # Drop policy start date and id columns
    df.drop(["Policy Start Date","id"],axis=1,inplace=True)

    return df

  def Prediction(self,df):
    df = self.MapTransform(df)

    filename = '/content/drive/MyDrive/Project3_Smart_Premium/dt_model.sav'
    model = pickle.load(open(filename, 'rb'))

    output = np.exp(model.predict(data))
    return output[0].round(2)


st.subheader("**Premium Amount Prediction**")

pid = st.text_input("Enter your ID")
age = st.text_input("Enter your Age")
gen = st.selectbox("Select your Gender",('Male','Female'))
income = st.text_input("Enter your Annual Income")
status = st.selectbox("Select your Marital Status",('Single', 'Married', 'Divorced'))
dep = st.selectbox("Select the Number of Dependents", (0,1,2,3,4))
edu = st.selectbox("Select your Education Level",('High School', "Bachelor's", "Master's", 'PhD'))
occ = st.selectbox("Select your Occupation",('Employed', "Unemployed", 'Self-Employed'))
hscore = st.text_input("Enter your Health Score")
st.caption("Enter values between 2-60 including decimals")
loc = st.selectbox("Select your Location",('Urban', "Rural", 'Suburban'))
ptype = st.selectbox("Select your Policy Type",('Premium', "Comprehensive", 'Basic'))
pclaims = st.selectbox("Select your Previous Number of Claims",(0,1,2,3,4,5,6,7,8,9))
vage = st.selectbox("Select your Vehicle Age in years",(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19))
cscore = st.text_input("Enter your Credit Score")
idur = st.selectbox("Select your Insurance Duration in years",(1,2,3,4,5,6,7,8,9))
pdate = st.date_input("Enter your Policy Start date",value=datetime.datetime.now())
st.caption("Enter date in the format YYYY/MM/DD")
smoke = st.selectbox("Do you have Smoking Habit?",('No','Yes'))
freq = st.selectbox("Select your Exercise Frequency",('Daily','Weekly','Monthly','Rarely'))
prop = st.selectbox("Select your Property Type",('House','Apartment','Condo'))
fb = st.selectbox("Select your Feedback	",('Good','Average','Poor'))

if 'clicked' not in st.session_state:
  st.session_state.clicked = False

def click_button():
  st.session_state.clicked = True

st.button('Submit', on_click=click_button)

if st.session_state.clicked:

  try:
    data=pd.DataFrame({'id' : [pid],'Age' : [age],'Gender': [gen],'Annual Income':[income],
                       'Marital Status' : [status], 'Number of Dependents' : [dep ],'Education Level' : [edu],
                       'Occupation': [occ],'Health Score': [hscore ],'Location': [loc],
                       'Policy Type':[ptype],'Previous Claims': [pclaims ],'Vehicle Age': [vage ],
                       'Credit Score': [cscore],'Insurance Duration':[idur],"Policy Start Date": [pdate],
                       'Customer Feedback': [fb],'Smoking Status': [smoke],'Exercise Frequency' : [freq],
                       'Property Type' : [prop]})
  except:
    st.write('After changing the details,Kindly click Submit button to predict your Mental Health!')

  convert_dict = {'Age': int, 'Number of Dependents': int, 'Previous Claims': int, 'Vehicle Age':int,
                'Insurance Duration': int,'Credit Score': int,'Annual Income':float, 'Health Score':float}
  data = data.astype(convert_dict)

  dc = DataCleaning()
  output = dc.Prediction(data)

  st.subheader(f"Your Predicted Premium Insurance Amount is {output}")

else:
  st.write('Kindly click Submit button to predict your Insurance cost!')

