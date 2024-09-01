import streamlit as st
from pydub import AudioSegment as AS
import io
import os


# Function definitions for audio conversion
def convert_audio_wav(input_file, output_file):
    audio = AS.from_file(input_file)
    audio.export(output_file + ".wav", format="wav")

def convert_audio_mp3(input_file, output_file):
    audio = AS.from_file(input_file)
    audio.export(output_file + ".mp3", format="mp3")

def convert_audio_flac(input_file, output_file):
    audio = AS.from_file(input_file)
    audio.export(output_file + ".flac", format="flac")

def convert_audio_ogg(input_file, output_file):
    audio = AS.from_file(input_file)
    audio.export(output_file + ".ogg", format="ogg")

# Streamlit App
st.title("Audio Converter App 🎧")
st.header("This app converts audio files to different formats.")
st.subheader("Made by: Hafiz Muhammad Kurniawan")
st.caption("This program python web app is made using Streamlit and Pydub.")
condistion = False

# File uploader
uploaded_file = st.file_uploader("Upload an audio file")

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/mp3")  # Display the audio file
    st.write("File uploaded successfully!")

    # Choose the output format
    format_option = st.selectbox("Select the output format", ("wav", "mp3", "flac", "ogg"))

    # Convert button
    if st.button("Convert"):
        output_file = "converted_audio"
        
        if format_option == "wav":
            convert_audio_wav(uploaded_file, output_file)
        elif format_option == "mp3":
            convert_audio_mp3(uploaded_file, output_file)
        elif format_option == "flac":
            convert_audio_flac(uploaded_file, output_file)
        elif format_option == "ogg":
            convert_audio_ogg(uploaded_file, output_file)
        
        st.success(f"File converted successfully to {format_option.upper()} format!")

        # Reload and display the converted audio
        with open(output_file + "." + format_option, "rb") as f:
            st.audio(f.read(), format=f"{format_option}")
        
        # Download button for the converted file
        with open(output_file + "." + format_option, "rb") as f:
            st.download_button(label="Download converted file", data=f, file_name=f"{output_file}.{format_option}")
        
        condistion = True


while(condistion==True):
    converted_file_path = "converted_audio" + "." + format_option if uploaded_file else None

    if converted_file_path and os.path.exists(converted_file_path):
        if st.button("Delete converted file"):
            os.remove(converted_file_path)
            st.warning("Converted file has been deleted.")
        break  # Exit the loop once the condition is met
    else:
        # Continue the loop and display an informational message if the file is not found
        st.info("Please upload and convert an audio file to enable the delete option.")
        break
