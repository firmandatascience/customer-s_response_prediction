import streamlit as st
import pandas as pd

#import library visualisasi
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    #buat judul
    st.title('Costumer Answer Prediction towards Deposit Campaign') #-> buat ngerun -> streamlit run *nama file* ->> eda.py
    st.sidebar.title('About this page')
    st.sidebar.write('This page is to predict the costumer answer towards deposit campaign.')


    'This is a string without str.write'

    #buat description atau print markdown biasa
    st.write('This is a example of Streamlit Description')



    #import image dari local
    st.image('image.jpeg', caption='', use_column_width=True)

    #nambahin subheader
    st.subheader('Data Information: ')

    #tambahin dataframe
    data = pd.read_csv('bank-full.csv', sep=';')
    #print
    st.dataframe(data)

    st.subheader('Data Visualization :')

    # menampilkan visualisasi costumer education level
    st.write('#### Costumer Education Level')
    fig = plt.figure()
    sns.countplot(data['education'])
    st.pyplot(fig)

    # menampilkan visualisasi housing vs loan
    st.write('#### Housing vs Loan')
    fig = plt.figure()
    sns.countplot(x=data['housing'], hue=data['loan'])
    st.pyplot(fig)


if __name__ == '__main__':
    run()