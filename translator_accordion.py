import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

FLAGS = {'ES': '🇪🇸', 'FR': '🇫🇷🇧🇪', 'NL': '🇳🇱🇧🇪', 'IT': '🇮🇹'}
LANG_CODES = {'ES': 'spanish', 'FR': 'french', 'NL': 'dutch', 'IT': 'italian'}
NOTICE_EN = (
    "machine translated. in case of doubt, please refer to the english version of this text, "
    "or get in contact with the People Team."
)

def translate(text, lang_code):
    # Preserve "People Team" during translation
    protected = "People Team"
    placeholder = "PEOPLETEAMPLACEHOLDER123"

    # Replace for translation
    safe_text = text.replace(protected, placeholder)
    notice_text = NOTICE_EN.replace(protected, placeholder)

    # Translate both
    translated_main = GoogleTranslator(source='auto', target=lang_code).translate(safe_text)
    translated_notice = GoogleTranslator(source='auto', target=lang_code).translate(notice_text)

    # Restore original
    translated_main = translated_main.replace(placeholder, protected)
    translated_notice = translated_notice.replace(placeholder, protected)

    return translated_main + "\n\n*_" + translated_notice + "_*"


st.set_page_config(page_title="🌍 4-Language Translator", layout="centered")
st.title("🌍 4-Language Translator")

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

        # Email button
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
