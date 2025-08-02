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
    translated_notice = translated_notice.repl
