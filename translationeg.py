from googletrans import Translator

def trans_eng_to_tel(data):
    translator = Translator()
    translated = translator.translate(data, src='en', dest='te')
    return translated.text

def trans_tel_to_eng(data):
    translator = Translator()
    translated = translator.translate(data, src='te', dest='en')
    return translated.text

english_sentences = [
    "Hello, how are you?",
    "I love programming.",
    "What's your name?",
    "The weather is nice today.",
    "How can I help you?"
]

telugu_sentences = [
    "నా వైద్యుడు దయగలవాడు",
    "గురువు బాగా బోధిస్తాడు",
    "ఆ వ్యక్తి నా న్యాయవాది",
    "ఆ ఇల్లు పెద్దది",
    "నువ్వేమి చేస్తున్నావు?"
]



telugu_translations = [trans_eng_to_tel(sentence) for sentence in english_sentences]

english_translations = [trans_tel_to_eng(sentence) for sentence in telugu_sentences]

for i in range(len(english_sentences)):
    print(f"English: {english_sentences[i]}")
    print(f"Telugu Translation: {telugu_translations[i]}\n")
    print(f"Telugu: {telugu_sentences[i]}")
    print(f"English Translation: {english_translations[i]}")
    