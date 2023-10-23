import streamlit as st

path = '数学一次方程式01_exported123.mp4'

st.header("Video動画の表示")

video_file = open(path, 'rb') #enter the filename with filepath

video_bytes = video_file.read() #reading the file

st.video(video_bytes) #displaying the video
