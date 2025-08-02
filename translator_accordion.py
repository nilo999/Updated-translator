import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# Set page config BEFORE anything else
st.set_page_config(page_title="🌍 4-Language Translator", layout="centered")

# Centered logo at top
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/nilo999/Updated-translator/main/DLLOGO.png" width="120">
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🌍 4-Language Translator")

# Updated flags
FLAGS = {'ES': '🇪🇸', 'FR': '🇫🇷🇧🇪🇨🇭', 'NL': '🇳🇱🇧🇪', 'IT': '🇮🇹🇨🇭'}
LANG_CODES = {'ES': 'spanish', 'FR': 'french', 'NL': 'dutch', 'IT': 'italian'}
NOTICE_EN = (
    "machine translated. in case of doubt, please refer to the english version of this text, "
    "or get in contact with the People Team."
)

# Smart translation function that protects “People Team”
def translate(text, lang_code):
    protected = "People Team"
    if protected in text:
        segments = text.split(protected)
        translated_segments = []
        for segment in segments:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(segment) if segment.strip() else ""
            translated_segments.append(translated)
        translated_main = f" {protected} ".join(translated_segments)
    else:
        translated_main = GoogleTranslator(source='auto', target=lang_code).translate(text)

    # Now for the notice
    if protected in NOTICE_EN:
        parts = NOTICE_EN.split(protected)
        translated_notice = f" {protected} ".join(
            GoogleTranslator(source='auto', target=lang_code).translate(part) if part.strip() else "" for part in parts
        )
    else:
        translated_notice = GoogleTranslator(source='auto', target=lang_code).translate(NOTICE_EN)

    return translated_main.strip() + "\n\n*_" + translated_notice.strip() + "_*"

# UI
input_text = st.text_area("✏️ Enter your English text here:", height=200)

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some English text above.")
    else:
        full_email_body = ""

        for lang, lang_name in LANG_CODES.items():
            with st.expander(f"{FLAGS[lang]} {lang}"):
                translated = translate(input_text, lang_name)
                st.markdown(translated)
                full_email_body += f"{lang} {FLAGS[lang]}\n{translated}\n\n"

        subject = urllib.parse.quote("Multilingual Translation")
        body = urllib.parse.quote(full_email_body)
        mailto_link = f"mailto:?subject={subject}&body={body}"

        st.markdown(f"""
            <div style="margin-top:30px">
            <a href="{mailto_link}" target="_blank" style="
                display: inline-block;
                background-color: #0078D4;
                color: white;
                padding: 12px 20px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
                font-size: 16px;
            ">✉️ Send All Translations via Outlook</a>
            </div>
        """, unsafe_allow_html=True)
