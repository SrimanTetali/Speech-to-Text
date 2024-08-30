from googletrans import Translator
import streamlit as st
import re
import language_tool_python

translator = Translator()
tool = language_tool_python.LanguageTool('en-US')

def preprocess_text(text):
    # Example preprocessing: Remove extra spaces and punctuation errors
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with single space
    return text

def postprocess_text(text):
    # Example postprocessing: Grammar correction using language_tool_python
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

def translate_text(text, src_language="te", dest_language="en"):
    try:
        text = preprocess_text(text)  # Preprocess text before translation
        translation = translator.translate(text, src=src_language, dest=dest_language)
        translated_text = translation.text
        translated_text = postprocess_text(translated_text)  # Postprocess after translation
        return translated_text
    except Exception as e:
        st.error(f"Translation Error: {e}")
        return "Translation Error"
