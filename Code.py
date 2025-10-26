import speech_recognition as sr
from googletrans import Translator

def voice_to_text_translation(target_lang="en"):
    recognizer = sr.Recognizer()
    translator = Translator()

    with sr.Microphone() as source:
        print("🎤 Speak something...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"🗣 Original Speech: {text}")

        translated = translator.translate(text, dest=target_lang)
        print(f"🌍 Translated Text ({target_lang}): {translated.text}")

    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError:
        print("⚠️ API request failed. Check your internet connection.")
    except Exception as e:
        print(f"⚡ Unexpected Error: {e}")

# Example: translate to Hindi (hi), Spanish (es), or English (en)
if __name__ == "__main__":
    voice_to_text_translation("hi")
