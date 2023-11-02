from googletrans import Translator
import re

# Function to translate English to Telugu
def trans_eng_to_tel(data):
    translator = Translator()
    translated = translator.translate(data, src='en', dest='te')
    return translated.text

# Function to translate Telugu to English
def trans_tel_to_eng(data):
    translator = Translator()
    translated = translator.translate(data, src='te', dest='en')
    return translated.text

# Function to perform basic gender debiasing
def debias_text(text):
    # Define a simple mapping of gendered terms to neutral terms
    gendered_terms = {
        'he': 'they',
        'his': 'their',
        'him': 'them',
        'she': 'they',
        'her': 'their',
        'hers': 'theirs'
    }

    # Use regular expressions to identify and replace gendered terms
    for gendered_term, neutral_term in gendered_terms.items():
        text = re.sub(r'\b' + gendered_term + r'\b', neutral_term, text, flags=re.IGNORECASE)
    
    return text

# List of 5 English sentences
english_sentences = [
    "doctor is working.",
    "I love programming.",
    "What's your name?",
    "The weather is nice today.",
    "How can I help you?"
]

# List of 5 Telugu sentences corresponding to the English sentences
telugu_sentences = [
    "నా వైద్యుడు దయగలవాడు",
    "గురువు బాగా బోధిస్తాడు",
    "ఆ వ్యక్తి నా న్యాయవాది",
    "ఆ ఇల్లు పెద్దది",
    "నువ్వేమి చేస్తున్నావు?"
]

# Translate from English to Telugu and perform gender debiasing
telugu_translations = [debias_text(trans_eng_to_tel(sentence)) for sentence in english_sentences]

# Translate from Telugu to English and perform gender debiasing
english_translations = [debias_text(trans_tel_to_eng(sentence)) for sentence in telugu_sentences]

# Print the results
for i in range(len(english_sentences)):
    print(f"Original English: {english_sentences[i]}")
    print(f"Original Telugu: {telugu_sentences[i]}")
    print(f"Debiased English Translation: {english_translations[i]}")
    print(f"Debiased Telugu Translation: {telugu_translations[i]}\n")