import streamlit as st
import speech_recognition as sr
from translator import translate_text

def transcribe_audio(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="te-IN")
    except sr.UnknownValueError:
        return "Unrecognized Speech"
    except sr.RequestError:
        return "Request Error"

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Please speak something...", icon="🎙️")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="te-IN")
            st.success(f"You said: {text}", icon="✅")
            
            translated_text = translate_text(text, src_language='te', dest_language='en')
            st.info(f"Translated to English: {translated_text}", icon="🌐")
            
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I did not understand the audio.", icon="❌")
        except sr.RequestError:
            st.error("Sorry, there was a problem with the Google Speech Recognition service.", icon="⚠️")
