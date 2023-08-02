import streamlit as st
from PIL import Image
import requests
from PIL import Image
from io import BytesIO


# Title
st.title("making a media file")
st.markdown("""
### 
coba membuat media file
=========================================================
""",True)
# Header
st.header("Belajar Bagaimana Menampilkan media di streamlit")

# 1. media gambar 
st.text('1. membuat media gambar')
# local
picture = Image.open('media/1.jpg')
st.image(picture, caption='ini wallpaper')

# # dari platform internet
# # URL gambar dari platform lain, misalnya dari suatu situs web
# image_url = 'https://unsplash.com/photos/the-sun-is-shining-through-the-clouds-in-the-sky-YCfUIt8i6hE'

# # Mengunduh gambar dari URL
# response = requests.get(image_url)
# image_data = response.content

# # Membuka gambar menggunakan PIL (Python Imaging Library)
# picture = Image.open(BytesIO(image_data))

# # Menampilkan gambar menggunakan st.image
# st.image(picture, caption='Ini gambar dari platform lain')
# 2. media audio
st.text('2. membuat media audio')
# local
# Open the audio file and read its content as binary data
audio = open('media/IPNU.mp3', 'rb')
audio_data = audio.read()

# Display the audio using st.audio
st.audio(audio_data, format='audio/mp3')
st.write('mars IPNU')
# online 

# 3 media video
st.text('3. membuat media video')
# dari local 
video = open('media/(20+) tom.mp4', 'rb', )
video1 = video.read()
st.video(video1)
# # dari online 
# # URL video dari YouTube atau platform lainnya
# video_url = 'https://www.youtube.com/watch?v=pYRZbkcyyOQ'

# # Display the video using st.video with the URL as an argument
# st.video(video_url)