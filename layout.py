import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import plotly_express as px
import time

# # Title
# st.title("making a layout dan container")
# st.markdown("""
# ### 
# coba membuat layout dan container
# =========================================================
# """,True)
# # Header
# st.header("Belajar Bagaimana Menampilkan layout dan container di streamlit")

# st.text('1. sidebar')
# st.text('2. navigation')

# st.text('==============================================================================================')
# cara menampilkan media layout dan container 
# sidebar radio
# test = st.sidebar.radio('navigation', ['Home','Colom','Tabs'])

# # sidebar selectbox
# st.sidebar.selectbox('navigation', ['NLP','FLASK','streamlit'])

# # sidebar multiselect
# st.sidebar.multiselect('navigation', ['NLP','FLASK','streamlit'])

# # sidebar input number
# st.sidebar.number_input('pilih tahun:', 2010,2022)

# # sidebar radio number
# st.sidebar.radio(label='navigation',options=[2010,2011,2012,2023])

# # sidebar file uploader
# st.sidebar.file_uploader('upload file', type=['csv','txt'])


test = st.sidebar.radio("Navigation", ['Home', 'Columns', 'Tabs', 'expander & container', 'Status Elements'])


if test == 'Home': 
        st.subheader('membuat halaman kolom, tabs, expander & kontainer :wave:')
    
        st.write('ini halaman home')
        st.write('................')
        
        st.header('coba di halaman home')
        st.write('################')
        st.write('''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus iaculis nulla lacus, interdum sagittis lectus mattis vitae. Nunc vel rhoncus mauris. Mauris luctus urna nibh, id luctus neque maximus vitae. Suspendisse pretium, nibh sed imperdiet accumsan, sem enim pharetra est, ac dictum lorem leo sed velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vestibulum eget risus tristique, eleifend erat nec, cursus odio. Aliquam mattis vel nunc sed sagittis. Donec eleifend euismod semper. Duis id est et enim sodales mollis. Morbi nec sagittis nisi, id posuere mi. Fusce bibendum turpis et leo varius varius. Pellentesque eget dolor vulputate, viverra justo in, convallis sapien. Nullam rutrum vestibulum vestibulum. Maecenas finibus nisi id tortor congue gravida.
            
            ''')
        st.header('Playlist Youtube')
        col1, col2, col3 = st.columns(3)
    
        with col1:
            st.subheader('youtube 1')
            st.video('https://www.youtube.com/watch?v=pYRZbkcyyOQ')
        
        with col2:
            st.subheader('youtube 2')
            st.video('https://www.youtube.com/watch?v=pYRZbkcyyOQ')
        
        with col3:
            st.subheader('youtube 3')
            st.video('https://www.youtube.com/watch?v=pYRZbkcyyOQ')

st.write('=================================')

# halaman colom 
if test == 'Columns':
    st.subheader('hai, ini mencoba bagian kolom')
    st.write('kita akan belajar membuat kolom')
    col1, col2 = st.columns([3,1])
    # get data from github
    data = pd.read_csv('https://raw.githubusercontent.com/jumadi-cloud/belajar_streamlit/master/dataset/datagaji1.csv')   

    col1.subheader('menampilkan data dengan grafik')
    col1.line_chart(data)

    col2.subheader('menampilkan data dengan tabel')
    col2.write(data)

# halaman Tabs
if test == 'Tabs':
    st.subheader('halo, sobat gurun')
    st.write('selanjutnya kita belajar fungsi tabs')
    
    # example by media 
    tab1, tab2, tab3 = st.tabs(['gambar 1', 'gambar 2', 'gambar 3'])
    
    # load gambar 
    gambar1 = Image.open('media/1.jpg')
    gambar2 = Image.open('media/1.jpg')
    gambar3 = Image.open('media/1.jpg')
    
    with tab1:
        st.header("Gambar 1")
        st.image(gambar1, width=200)
        
    with tab2:
        st.header("Gambar 2")
        st.image(gambar2, width=200)
    
    with tab3:
        st.header("Gambar 3")
        st.image(gambar3, width=200)
    
    # example with dataset
    tab1, tab2 =st.tabs(['chart', 'data'])
    data = pd.read_csv('https://raw.githubusercontent.com/jumadi-cloud/belajar_streamlit/master/dataset/datagaji1.csv') 
    
    tab1.subheader('menampilkan data by chart')
    tab1.line_chart(data)
    
    tab2.subheader('menampilkan data by tabel')
    tab2.write(data)
    
# halaman expander & container
if test == 'expander & container':
        st.subheader('halo, sobat gurun')
        st.write('selanjutnya kita belajar fungsi expender dan container')
        # get data
        data = pd.read_csv('https://raw.githubusercontent.com/jumadi-cloud/belajar_streamlit/master/dataset/datagaji1.csv')
        gambar1 = Image.open('media/1.jpg')
        
        # example expander
        st.bar_chart(data)
        with st.expander('this is expander'):
            st.write('''
                    ini adalah contoh dari expander
                    kita menvisualisasikan dengan data gaji 
                    ''')
            st.image(gambar1)
        
        #exampe container 
        with st.container():
            st.write('this is a container')
            st.bar_chart(data)
        st.write('this is no container')
    
if test == "Status Elements":
    st.subheader('halo, sobat gurun')
    st.write('selanjutnya kita belajar fungsi expender dan container')
    
    # example fungsi progres
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)
    
    #fungsi baloon
    st.balloons()
    
    # Contoh Fungsi Error, Success, Info, Exception dan Warning
    st.error("Ini Adalah Contoh Fungsi Dari Error")
    st.success("Ini Adalah Contoh Fungsi Dari Success", icon="✅")
    st.info("Ini Adalah Contoh Fungsi Dari Info")
    st.exception(RuntimeError("Ini Adalah Contoh Dari Erorr"))
    st.warning("Ini Adalah Contoh Fungsi Dari Warning")
    
    #example spinner
    with st.spinner('Wait for it...'):
        time.sleep(5)
    st.success('Done!')
