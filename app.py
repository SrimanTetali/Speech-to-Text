import streamlit as st
from stt import speech_to_text
from accuracy_test import test_stt_accuracy
import styles

# Streamlit UI
st.set_page_config(page_title="Speech to Text Converter", page_icon="🎤", layout="centered")

# Load Custom CSS
st.markdown(styles.load_css(), unsafe_allow_html=True)

# Header Section
st.title("🗣️ Speech to Text Converter")
st.markdown("""
### Effortlessly Convert Your Speech into Text
Speak clearly into your microphone and let the app transcribe your words into text.
""")

# Create a dropdown for selecting the view
option = st.sidebar.selectbox(
    "Select an option",
    ["Converter", "Accuracy Test"],
    index=0
)

# Display the relevant content based on the dropdown selection
if option == "Converter":
    st.markdown("---")
    if st.button("🎤 Click to Speak", key="record_button"):
        speech_to_text()

elif option == "Accuracy Test":
    st.markdown("---")
    st.markdown("### Test Speech-to-Text Accuracy with Sample Audio Files")
    
    test_data = [
        ("./Audios/s1.wav", "ఈ వివాదం సెప్టెంబర్ రెండు వేల తొమ్మిదిన పరిష్కారమైనది"),
        ("./Audios/s2.wav", "ఒక బ్యాంకు ఒక ప్రాథమిక పాఠశాల ఉన్నాయి"),
        ("./Audios/s3.wav", "చాలా గొంగళి పురుగులు షాకాహారులే"),
        ("./Audios/s4.wav", "ప్రిన్సిపాల్ ఒక మొమెంటోతో ప్రవేశించారు"),
        ("./Audios/s5.wav", "ట్రూమాన్ లైబ్రరీ అండ్ మ్యూజియం"),
        ("./Audios/s6.wav", "దాదాసాహెబ్ ఫాల్కే అవార్డు గ్రహీత శాంతారాం"),
        ("./Audios/s7.wav", "అతని కుమార్తెను దొంగలు అపహరిస్తారు"),
        ("./Audios/s8.wav", "ఈ సంబంధం రెండు వెలు తొమ్మిది ఫిబ్రవరిలో ముగిసింది"),
        ("./Audios/s9.wav", "ఏటా ఇక్కడ జాతర కూడా ఘనంగా నిర్వహిస్తారు"),
        ("./Audios/s10.wav", "పిన్ కోడ్ అయిదు లక్షలు ఎనిమిది వేల రెండు వందల నాలుగు"),
        ("./Audios/s11.wav", "దీని ముఖ్య విషయాలు పిల్లల మానసిక శాస్త్రము మరియు సామాజిక మానసిక శాస్త్రము"),
        ("./Audios/s12.wav", "ఈ కమిటీ యందు ఇరవై ఒకటి రాష్ట్ర పార్టీలుంటాయి"),
        ("./Audios/s13.wav", "ఈ సమయంలో దాసరి నారాయణరావు కె.రాఘవేంద్రరావు కోడిరామి రెడ్డి అగ్రస్థానంలో ఉన్న దర్శకులు"),
        ("./Audios/s14.wav", "చెరువు కట్ట మీద పోలేరమ్మ గుడి ఉన్నది"),
    ]

    if st.button("Test Accuracy", key="test_button"):
        st.markdown("### Results")
        test_stt_accuracy(test_data)

# Hide Streamlit's default footer and menu
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
