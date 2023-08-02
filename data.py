# import module
import streamlit as st  
import pandas as pd
import numpy as np
# title 
st.title('percobaan menampilkan data')

# markdown 
st.markdown('''
            percobaan menampilkan 
            - membuat array
            - membuat tipe data series
            - menampilkan dataset dari github
            
            ''',True)

# header 
st.header('belajar insert data')

# buat data 
a = np.array([1,2,3,4,5])
b = np.array([[1.2,1.2,2], [1.1,2,2.2]],dtype=float)
# belajar membuat data array
u = pd.Series([1,2,3,4,5,6,7,8])
# mengambil dataset dari github
datset = pd.read_csv("https://raw.githubusercontent.com/krishnaik06/simple-Linear-Regression/master/Salary_Data.csv")
# membuat data dictionary
profile = {
    'nama': 'lord',
    'umur': '30',
    'pemrograman': ['python','streamlit','dan mencintaimu'],
    'favorit':{
        'makanan': 'indomei dobel',
        'hobi': 'rebahan'
    }
    
}
# ===============================

# cara menampilkan data

# dataframe
st.text('ini dataFrame')
st.dataframe(b)
st.dataframe(u)
st.dataframe(datset)

# tabel 
st.text('ini adalah data tabel')
st.table(a)
st.table(datset)
# file json
st.text('menampilkan data json')
st.json(profile)
# matric
st.text('menampilkan data matrix')
st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")