import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# --- Setup ---
st.set_page_config(page_title="🌍 4-Language Translator", layout="centered")

# --- Logo at the top ---
st.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <img src="https://raw.githubusercontent.com/nilo999/Updated-translator/main/DLLOGO.png" width="120">
    </div>
""", unsafe_allow_html=True)

st.title("🌍 4-Language Translator")

# --- Flags ---
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

NOTICE_EN = "Translated by artificial intelligence. In case of doubt, please refer to the English version of this text, or get in contact with the People Team."


# --- Translation function ---
def translate(text, lang_code):
    protected = "People Team"
    placeholder = "PEOPLETEAM_XYZ_123"

    # Replace protected phrase
    text_safe = text.replace(protected, placeholder)
    notice_safe = NOTICE_EN.replace(protected, placeholder)

    # Translate main content and notice
    translated_main = GoogleTranslator(source='auto', target=lang_code).translate(text_safe)
    translated_notice = GoogleTranslator(source='auto', target=lang_code).translate(notice_safe)

    # Restore protected phrase
    translated_main = translated_main.replace(placeholder, protected)
    translated_notice = translated_notice.replace(placeholder, protected)

    return translated_main.strip() + "\n\n*_" + translated_notice.strip() + "_*"


# --- UI ---
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

        # Prepare mailto link
        subject = urllib.parse.quote("Multilingual Translation")
        body = urllib.parse.quote(full_email_body)
        mailto_link = f"mailto:?subject={subject}&body={body}"

        # Outlook button
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
