import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Dictionary of supported languages and their codes
LANGUAGES = {
    'tamil': 'ta',
    'french': 'fr',
    'spanish': 'es',
    'hindi': 'hi',
    'german': 'de',
    'japanese': 'ja',
    'english': 'en',
    # Add more languages as needed
}


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for speech...")

        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.RequestError:
            print("API was unreachable or unresponsive")
        except sr.UnknownValueError:
            print("Unable to recognize speech")

    return None


def translate_text(text, target_language):
    translator = Translator()
    # Auto-detect source language and translate to the target language
    translation = translator.translate(text, dest=target_language)
    print(f"Detected language: {translation.src}")
    print(f"Translated text: {translation.text}")
    return translation.text


def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_language_code():
    print("Available languages: ", ", ".join(LANGUAGES.keys()))
    language = input("Enter the language you want to translate to: ").lower()

    # Check if the input language is valid
    if language in LANGUAGES:
        return LANGUAGES[language]
    else:
        print("Sorry, that language is not supported.")
        return None


def get_input_method():
    choice = input("Choose input method (text/speech): ").lower()
    if choice in ["text", "speech"]:
        return choice
    else:
        print("Invalid choice. Please choose either 'text' or 'speech'.")
        return get_input_method()


if __name__ == "__main__":
    print("Real-Time Speech Recognition and Translation")

    # Step 1: Choose Input Method
    input_method = get_input_method()

    if input_method == "text":
        spoken_text = input("Enter the text you want to translate: ")
    elif input_method == "speech":
        spoken_text = recognize_speech()

    if spoken_text:
        # Step 2: Select Target Language
        target_language = get_language_code()

        if target_language:
            # Step 3: Translate Text to Selected Language
            translated_text = translate_text(spoken_text, target_language=target_language)

            # Step 4: Convert Translated Text to Speech
            text_to_speech(translated_text)
