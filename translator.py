from translate import Translator

def get_language_code(lang_name):
    """Returns the language code for a given language name."""
    languages = {
        'english': 'en',
        'spanish': 'es',
        'russian': 'ru',
        # Add more languages and their codes here
    }
    return languages.get(lang_name.lower())

def translate_text():
    while True:
        text = input('Enter your text that you want to be translated (or type "exit" to quit): ')
        if text.lower() == "exit":
            break
        print('Available languages: English, Spanish, Russian')
        language_name = input('Choose language that you want to translate to: ')
        language_code = get_language_code(language_name)
        if language_code:
            translator = Translator(to_lang=language_code)
            try:
                translation = translator.translate(text)
                print(f'Translated text: {translation}')
            except Exception as e:
                print(f"Error during translation: {e}")
        else:
            print("Language not supported or wrong language name.")
        print("\n")

# Run the translation application
translate_text()





