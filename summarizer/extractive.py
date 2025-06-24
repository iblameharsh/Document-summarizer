import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nltk.download("punkt_tab")

def extractive_summary(text, num_sentences=3):
    sentences = nltk.sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text

    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix)

    scores = similarity_matrix.sum(axis=1)
    top_indices = np.argsort(scores)[-num_sentences:]
    top_indices.sort()

    return ' '.join([sentences[i] for i in top_indices])
