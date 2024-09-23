import streamlit as st
import eda2, predict2

st.set_page_config(
    page_title='Costumer Answer Prediction towards Deposit Campaign',
    layout='wide',
    initial_sidebar_state='expanded'
    # page_icon=
)

st.sidebar.title('Navigation')
select = st.sidebar.selectbox(label='Pilih Page', options= ['EDA', 'Predict'])

if select == 'EDA':
    eda2.run()
else: 
    predict2.run()

