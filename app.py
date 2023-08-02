# import modul 
import streamlit as st
import emoji
# title
st.title('_ini adalah judul with_ :blue[colors] and emojis :sunglasses:')

# header
st.header('belajar streamlit first')
# sub header 
st.subheader('yok kita coba mari bersama kawan')
# text 
st.text('mari coba belajar bersama kami')
# markdown
st.markdown('# markdown1')
st.markdown('## markdown1')
st.markdown('### markdown1')
st.markdown('#### markdown1')

# markdown multibars
st.markdown('''
            # test1
            
            ## test2
            
            ### test3
            
            #### test4
            ''',True)

# code block 
st.code('halooo dek!!!!')

# latex
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# devider
st.write("slider baru time.")

st.slider("ini adalah range", 0, 100, (25, 75))

st.divider()  # 👈 Draws a horizontal rule

st.write("This text is between the horizontal rules.")

st.divider()  # 👈 Another horizontal rule