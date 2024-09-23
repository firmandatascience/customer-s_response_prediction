import streamlit as st
import pandas as pd
import pickle 
import json
import numpy as np

def run():
    st.title('Costumer Answer Prediction towards Deposit Campaign')
    # load model

    # load model yang udah dibuat
    with open('best_model_gb.pkl', 'rb') as file_3:
        model = pickle.load(file_3)

    # membuat form untuk input data
    st.write('## Input Data')
    # form input data
    with st.form(key='costumer'):
        age = st.number_input('Age', min_value=10, max_value=100)
        job = st.selectbox('Job', ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown'])
        marital = st.selectbox('Marital', ['divorced', 'married', 'single', 'unknown'])
        education = st.selectbox('Education', ['unknown', 'primary', 'secondary', 'tertiary'])
        default = st.selectbox('Default', ['no', 'yes'])
        housing = st.selectbox('Housing', ['no', 'yes'])
        loan = st.selectbox('Loan', ['no', 'yes'])
        contact = st.selectbox('Contact', ['cellular', 'telephone'])
        month = st.selectbox('Month', ['apr', 'aug', 'dec', 'jul', 'jun', 'mar', 'may', 'nov', 'oct', 'sep'])
        day_of_week = st.selectbox('Day of Week', ['fri', 'mon', 'thu', 'tue', 'wed'])
        duration = st.number_input('Duration', min_value=0, max_value=5000)
        campaign = st.number_input('Campaign', min_value=0, max_value=50)
        pdays = st.number_input('Pdays', min_value=0, max_value=1000)
        previous = st.number_input('Previous', min_value=0, max_value=10)
        poutcome = st.selectbox('Poutcome', ['unknown', 'failure', 'other' ,'success'])
        
        # submit button
        submit = st.form_submit_button(label='Predict')

    if submit:
        data = {
            'age': age,
            'job': job,
            'marital': marital,
            'education': education,
            'default': default,
            'housing': housing,
            'loan': loan,
            'contact': contact,
            'month': month,
            'day_of_week': day_of_week,
            'duration': duration,
            'campaign': campaign,
            'pdays': pdays,
            'previous': previous,
            'poutcome': poutcome
        }

        df = pd.DataFrame(data, index=[0])
        prediction = model.predict(df)[0]
        st.write('Prediction: ', prediction)

        # menyimoan hasil prediksi
        prediction = model.predict(df)[0]
        if prediction == 0:
            prediction = 'No'
        else:
            prediction = 'Yes'

        st.write('Prediction: ', prediction)

if __name__ == '__main__':
    run()
