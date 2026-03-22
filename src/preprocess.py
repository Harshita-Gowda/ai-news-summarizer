import nltk
import re

# Download required NLTK data safely (works locally + cloud)
def download_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except:
        nltk.download('punkt_tab')

    try:
        nltk.data.find('corpora/stopwords')
    except:
        nltk.download('stopwords')

# Call the downloader
download_nltk()

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))


# Clean the text (remove extra spaces)
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# Split into sentences
def get_sentences(text):
    return sent_tokenize(text)


# Split into words
def get_words(text):
    return word_tokenize(text.lower())