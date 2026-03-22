import nltk
from collections import Counter

def download_nltk():
    try:
        nltk.data.find('corpora/stopwords')
    except:
        nltk.download('stopwords')

download_nltk()

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

# Better filtering
extra_stopwords = {
    "said", "also", "would", "could",
    "world", "first", "today", "stunned",
    "tokyo", "move", "morning"
}

def extract_keywords(words, top_n=5):

    filtered = [
        word for word in words
        if word.isalnum()
        and word not in stop_words
        and word not in extra_stopwords
        and len(word) > 4
    ]

    freq = Counter(filtered)

    keywords = [word for word, _ in freq.most_common(top_n)]

    return keywords