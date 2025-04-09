import pickle # pre traines model loading
import streamlit as st  # web app
from streamlit_option_menu import option_menu

st.set_page_config(layout='wide')

heart_disease_model= pickle.load(open(r"C:\Users\hp\OneDrive\Documents\Predictions\training_models\Heart_model.sav",'rb'))


with st.sidebar:
     selected= option_menu('Prediction of disease outbreak system',['Diabetes Prediction','Heart Disease Prediction'],
                           menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)


if selected == "Heart Disease Prediction":
   st.title('Heart Disease Prediction Using ML')
   col1,col2,col3,col4 = st.columns(4)
   with col1:
        Age = st.text_input('Age')
   with col2:
        Sex = st.text_input('Sex - M = 1 & F = 0')
   with col3:
        cp = st.text_input('Chest Pain')
   with col4:
        trestbps = st.text_input('Resting Blood Pressure')
   with col1:
        chol = st.text_input('Cholestrol')
   with col2:
        fbs = st.text_input('Fasting Blood Sugar')
   with col3:
        restecg = st.text_input('RestECG')
   with col4:
        thalang = st.text_input('Thalach')
   with col1:
        exang = st.text_input('Exang')
   with col2:
        oldpeak = st.text_input('OldPeak')
   with col3:
        slope = st.text_input('Slope')
   with col4:
        ca = st.text_input('Ca')
   with col1:
        thal = st.text_input('Thal')
   
heart_diagnosis = ''
if st.button('Heart Test Result'):
   user_input=[Age,Sex,cp, trestbps, chol, fbs, restecg, thal]
   if   user_input[1] == 'M':
        user_input[1] = 1  # Male = 1
   elif user_input[1] == 'F':
        user_input[1] = 0  # Female = 0
   user_input=[float(x) for x in user_input]
   heart_prediction = heart_disease_model.predict([user_input])
   if heart_prediction[0]==1:
      heart_diagnosis= 'Person has heart disease'
   else:
      heart_diagnosis= 'Person has not heart disease'
   st.success(heart_diagnosis)  
