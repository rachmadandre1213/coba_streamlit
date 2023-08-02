import streamlit as st
# Title
st.title("making a button")
st.markdown("""
### 
coba membuat widget
=========================================================
""",True)
# Header
st.header("Belajar Bagaimana Menampilkan widget di streamlit")

# 1. create button 
st.text("1. ini contoh create button ")

result = st.button("klik disini")
st.write(result)
if result:
    st.write(":smile:")
# 2. create checkbox
st.text("2. ini contoh create cekbox")
if st.checkbox('show/hide'):
    st.text('halo sobat belajar, salam sejahtera')


# 3. create radio button 
st.text("3. ini contoh radio button")
status  = st.radio('pilih status:',
        ('jomblo','married','janda','duda'))
# menampilkan
st.write("pilih kondisi sekarang:",status)

# 4. create select box
st.text("4. ini contoh select box")

domain = st.selectbox("kami siap belajar materi:",
                    ['DS','ML','flask','streamlit'])
st.write("kami siap belajar materi:",domain)

# 5. create multi select
st.text("5. ini contoh multi select")

domain = st.multiselect("kami siap belajar materi:",
                    ['DS','ML','flask','streamlit'])
st.write("kami siap belajar materi:",len(domain), 'playlist')
# 6. create slider 
st.text("6. ini contoh slider")

Umur = st.slider('berapa umur anda sekarang',0,65)

st.text('umur saya sekarang:{}'.format(Umur))
# 7. create select slider
st.text("7. ini contoh select slider")

city = st.select_slider('pilih nama kota',
                options=['jakarta','surabaya','sidoarjo','gresik'])
st.write('pilih tempat tinggalmu:',city)
# 8. create input text
st.text("8. ini contoh input text")
title = st.text_input('dimana Tempat Tinggal kamu', '')

st.write('Tempat Tinggal kamu di', title)

# 9. create input nomer
st.text("9. ini contoh input nomer")
number = st.number_input('Insert a number',1,10000)
st.write('The max number is ', number)
# 10. create text area 
st.text("10. ini contoh text area")
text = st.text_area('silahkan masukan kota anda','')
st.write('kota anda di:',text)

# 11. create date input
st.text('11. ini adalah input tanggal')
birthday = st.date_input('tanggal berapa kamu lahir?')
st.write('tanggal lahir saya adalah:',birthday)
# 12. create input time 
st.write('12. contoh masukan waktu')
time = st.time_input('setting waktu pagi hari')
st.write('bangunkan pukul 8.45', time)
# 13 create file uploader
st.text('13. membuat file uploader')
upload = st.file_uploader('upload file', type=['csv','pdf','txt'])

# 14 create color picker
st.text('14. membuat pilihan warna')
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


