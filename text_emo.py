from transformers import pipeline
import googletrans

translator = googletrans.Translator()
classifier = pipeline("sentiment-analysis", model="./emotion_text_classifier")

def apply(text):
    text = translator.translate(text).text
    return classifier([text])[0]