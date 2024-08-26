import streamlit as st
from jiwer import wer
from stt import transcribe_audio
from translator import translate_text

def test_stt_accuracy(test_data):
    total_wer = 0
    for audio_file, ground_truth in test_data:
        transcribed_text = transcribe_audio(audio_file)
        error_rate = wer(ground_truth, transcribed_text)
        total_wer += error_rate

        st.write(f"**Audio File:** {audio_file}")
        st.write(f"**Actual Text:** {ground_truth}")
        st.write(f"**Transcribed Text:** {transcribed_text}")
        
        # Translate transcribed text
        translated_text = translate_text(transcribed_text)
        st.write(f"**Translated Text:** {translated_text}")
        st.write(f"**WER:** {error_rate:.2f}")
        st.markdown("---")

    average_wer = total_wer / len(test_data)
    average_accuracy = 100 - (average_wer * 100)
    st.write(f"### **Average Accuracy:** {average_accuracy:.2f}%")
