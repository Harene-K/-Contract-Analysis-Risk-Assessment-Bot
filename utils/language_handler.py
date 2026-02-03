from langdetect import detect
from googletrans import Translator

translator = Translator()

def detect_and_normalize(text):
    try:
        language = detect(text)
    except:
        language = "en"

    if language == "hi":
        translated = translator.translate(text, src="hi", dest="en").text
        return translated, "Hindi"

    return text, "English"
