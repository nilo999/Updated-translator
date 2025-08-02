import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# Set page config once at the very top
st.set_page_config(page_title="🌍 4-Language Translator", layout="centered")

# Show logo once at the top of the app
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/nilo999/Updated-translator/main/DLLOGO.png" width="120">
    </div>
    """,
    unsafe_allow_html=True
)

st.title("🌍 4-Language Translator")

FLAGS = {
    'ES': '🇪🇸',
    'FR': '🇫🇷🇧🇪🇨🇭',
    'NL': '🇳🇱🇧🇪',
    'IT': '🇮🇹🇨🇭',
}

LANG_CODES = {
    'ES': 'spanish',
    'FR': 'french',
    'NL': 'dutch',
    'IT': 'italian',
}

# Notice with 'People Team' preserved
NOTICE_EN = (
    "Translated by artificial intelligence. "
    "In case of doubt, please refer to the English version of this text, or get in contact with your local HR Representative."
)

def translate(text, lang_code):
    protected = "People Team"
    placeholder = "PEOPLETEAMPLACEHOLDER123"

    # Replace protected phrase with placeholder before translation
    safe_text = text.replace(protected, placeholder)
    notice_text = NOTICE_EN.replace(protected, placeholder)

    # Translate main text and notice separately
    translated_main = GoogleTranslator(source='auto', target=lang_code).translate(safe_text)
    translated_notice = GoogleTranslator(source='auto', target=lang_code).translate(notice_text)

    # Restore protected phrase in both translations
    translated_main = translated_main.replace(placeholder, protected)
    translated_notice = translated_notice.replace(placeholder, protected)

    return translated_main.strip() + "\n\n*_" + translated_notice.strip() + "_*"


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

        # Add the original English text at the end (italic, in brackets)
        original_notice = f"\n\n*_(Original text: {input_text.strip()})_*"
        full_email_body += original_notice



        subject = urllib.parse.quote("Multilingual Translation")
        body = urllib.parse.quote(email_body_with_logo)
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
