import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# ---- Page Setup ----
st.set_page_config(page_title="🌍 4-Language Translator", layout="centered")

# ---- Logo ----
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/nilo999/Updated-translator/main/DLLOGO.png" width="120">
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🌍 4-Language Translator")

# ---- Language Settings ----
FLAGS = {
    'ES': '🇪🇸',
    'FR': '🇫🇷🇧🇪🇨🇭',
    'NL': '🇳🇱🇧🇪',
    'IT': '🇮🇹🇨🇭'
}

LANG_CODES = {
    'ES': 'spanish',
    'FR': 'french',
    'NL': 'dutch',
    'IT': 'italian'
}

NOTICE_EN = (
    "machine translated. in case of doubt, please refer to the english version of this text, "
    "or get in contact with the People Team."
)

# ---- Translation Function ----
def translate(text, lang_code):
    protected = "People Team"
    
    # ---- Main Body ----
    if protected in text:
        parts = text.split(protected)
        translated_parts = []
        for part in parts:
            translated_parts.append(
                GoogleTranslator(source='auto', target=lang_code).translate(part) if part.strip() else ""
            )
        translated_main = f" {protected} ".join(translated_parts)
    else:
        translated_main = GoogleTranslator(source='auto', target=lang_code).translate(text)

    # ---- Notice ----
    if protected in NOTICE_EN:
        parts = NOTICE_EN.split(protected)
        translated_notice_parts = []
        for part in parts:
            translated_notice_parts.append(
                GoogleTranslator(source='auto', target=lang_code).translate(part) if part.strip() else ""
            )
        translated_notice = f" {protected} ".join(translated_notice_parts)
    else:
        translated_notice = GoogleTranslator(source='auto', target=lang_code).translate(NOTICE_EN)

    return translated_main.strip() + "\n\n*_" + translated_notice.strip() + "_*"

# ---- Input Area ----
input_text = st.text_area("✏️ Enter your English text here:", height=200)

# ---- Translate Button ----
if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some English text above.")
    else:
        full_email_body = ""

        for lang, lang_name in LANG_CODES.items():
            with st.expander(f"{FLAGS[lang]} {lang}"):
                translated = translate(
