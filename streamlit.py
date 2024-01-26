import streamlit as st
import time

st.title("Try this question :smile:")

a = ['215', '315', '351', '265']
ans = st.radio("What is 25% of 1260?", a, None)


def audio(audiopath):
    audio_file = open(audiopath, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg', start_time = 0)

@st.cache_data
def image(imagepath):
    st.image(imagepath, caption='dancing_boy_meme')


if ans == a[1]:
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
    # Update the progress bar with each iteration.
        latest_iteration.text(f'Loading {i+1}%')
        bar.progress(i+1)
        time.sleep(0.05)
    #audio
    audio("rightanswer.ogg")
    #image
    
    # time.sleep(4.5)
    # st.image('dance-meme.gif', caption='Sunrise by the mountains')
    agree = st.checkbox('I agree')
    if agree:
        image("dance-meme.gif")
if ans == a[0] or ans == a[2] or ans == a[3]:
    time.sleep(2)
    audio("wronganswer.ogg")
    # time.sleep(3)


