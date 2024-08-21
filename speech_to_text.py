import streamlit as st 
import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        st.info("Please speak something...")

        # Adjust for ambient noise and record the audio
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio, language="hi-IN")
            st.success(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I did not understand the audio.")
        except sr.RequestError:
            st.error("Sorry, there was a problem with the Google Speech Recognition service.")

# Streamlit interface
st.title("Speech to Text")

# Button to trigger speech recognition
if st.button("Click to Speak"):
    speech_to_text()