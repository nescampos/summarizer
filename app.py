import os
import streamlit as st
from elevenlabs import set_api_key, generate, save
import cohere
from PIL import Image


cohere_api_key = st.secrets["cohere_api_key"]
elevenlabs_api_key = st.secrets["elevenlabs_api_key"]

set_api_key(elevenlabs_api_key)
co = cohere.Client(cohere_api_key)


# Configure the UI
image = Image.open('logo.png')
st.set_page_config(page_title="Summarizer")

st.image(image, caption='')


html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

with st.sidebar:
    st.markdown("""
    # About 
    Summarizer is a helper tool built with [ElevenLabs](https://elevenlabs.io/) and [Cohere](https://cohere.com/) to help summarize long texts and listen to a synthesis of them.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Enter the texto about your request. And wait for the audio with the summary.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by [Néstor Campos](https://www.linkedin.com/in/nescampos/)
    """,
    unsafe_allow_html=True,
    )
st.markdown("""
# Summarizer
""")

st.markdown("""
### Get a spoken summary of your texts.
""")

large_text = st.text_area("Enter the text you want to summarize: ", placeholder="All the information about the content you want to synthesize in one summary..")


if st.button("Generate and listen to the summary"):
    response = co.summarize( 
        model='summarize-medium', 
        length='short',
        extractiveness='medium',
        format='paragraph',
        text=large_text
    )
    summary = response.summary
    audio = generate(
        text=summary,
        voice="Bella",
        model='eleven_monolingual_v1'
    )

    save(audio, "./output.mp3")
    audio_file = open('./output.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.text(f"Summary:\n\n{summary}\n\n")
    st.audio(audio_bytes, format='audio/mpeg')
