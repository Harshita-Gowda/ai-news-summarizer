from collections import defaultdict
import nltk

# Safe NLTK downloads
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

download_nltk()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))


def summarize(text, sentences, num_sentences=3):

    word_freq = defaultdict(int)
    words = word_tokenize(text.lower())

    for word in words:
        if word.isalnum() and word not in stop_words:
            word_freq[word] += 1

    sentence_scores = defaultdict(int)

    for i, sent in enumerate(sentences):

        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                sentence_scores[sent] += word_freq[word]

        # Headline boost
        if i == 0:
            sentence_scores[sent] *= 1.5

        # Boost numeric sentences
        if any(char.isdigit() for char in sent):
            sentence_scores[sent] *= 1.3

    # Normalize
    for sent in sentence_scores:
        length = len(word_tokenize(sent))
        if length > 0:
            sentence_scores[sent] /= length

    summary_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:num_sentences]

    return summary_sentences