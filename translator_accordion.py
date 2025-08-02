import streamlit as st
from deep_translator import GoogleTranslator
import urllib.parse

# Flags and language codes
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

# Notice message (English)
NOTICE_EN = (
    "Translated by artificial intelligence. "
    "In case of doubt, please refer to the English version of this text, "
    "or get in contact with your local HR Representative."
)

# Function to translate text while protecting "People Team"
def translate(text, lang_code):
    protected = "People Team"
    placeholder = "PEOPLETEAMPLACEHOLDER123"

    # Replace protected phrase with placeholder to avoid translation
    safe_text = text.replace(protected, placeholder)
    safe_notice = NOTICE_EN.replace(protected, placeholder)

    # Translate main text and notice
    translated_main = GoogleTranslator(source='auto', target=lang_code).translate(safe_text)
    translated_notice = GoogleTranslator(source='auto', target=lang_code).translate(safe_notice)

    # Restore protected phrase
    translated_main = translated_main.replace(placeholder, protected)
    translated_notice = translated_notice.replace(placeholder, protected)

    # Return combined translation with italicized notice
    return translated_main.strip() + "\n\n*_" + translated_notice.strip() + "_*"

# Streamlit page config
st.set_page_config(page_title="People Team Translator", page_icon="🧑‍💼")

# App UI
st.title("🌍 4-Language Translator")

input_text = st.text_area("✏️ Enter your English text here:", height=200)

if st.button("Translate"):
    if not input_text.strip():
        st.warning("Please enter some English text above.")
    else:
        full_email_body = ""
        for lang, lang_code in LANG_CODES.items():
            with st.expander(f"{FLAGS[lang]} {lang}"):
                translated = translate(input_text, lang_code)
                st.markdown(translated)
                full_email_body += f"{FLAGS[lang]} {lang}\n{translated}\n\n"
        
        # Add original text at the end in italics with label
        original_notice = f"\n\n*_(Original text: {input_text.strip()})_*"
        full_email_body += original_notice
        
        # Create mailto link
        subject = urllib.parse.quote("Translated Texts from People Team")
        body = urllib.parse.quote(full_email_body)
        mailto_link = f"mailto:?subject={subject}&body={body}"

        st.markdown(f"""
            <div style="margin-top:30px">
                <a href="{mailto_link}" target="_blank" style="
                    display: inline-block;
                    background-color: #0078D4;
                    color: white;
                    padding: 10px 20px;
                    text-decoration: none;
                    border-radius: 5px;
                ">📧 Send Translations by Email</a>
            </div>
        """, unsafe_allow_html=True)

# Replace st.experimental_user with st.user if used anywhere else in your app
# Example usage (optional):
# user = st.user
# if user:
#     st.write(f"Hello, {user.name}!")
