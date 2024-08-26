from googletrans import Translator
import streamlit as st

translator = Translator()

def translate_text(text, src_language="te", dest_language="en"):
    try:
        translation = translator.translate(text, src=src_language, dest=dest_language)
        return translation.text
    except Exception as e:
        st.error(f"Translation Error: {e}")
        return "Translation Error"
