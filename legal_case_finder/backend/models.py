import pandas as pd
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics.pairwise import cosine_similarity

# ── Load & clean ──────────────────────────────────────────
df = pd.read_csv('dataset/legal_text_classification.csv')

# Drop missing text
df = df.dropna(subset=['case_text'])

# Keep only top 7 outcomes
keep = ['cited','referred to','applied','followed',
        'considered','discussed','distinguished']
df = df[df['case_outcome'].isin(keep)].reset_index(drop=True)

print(f"✅ Dataset ready: {len(df)} cases, {df['case_outcome'].nunique()} outcomes")

# ── Clean text ────────────────────────────────────────────
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = [w for w in text.split() if w not in stop_words]
    return ' '.join(words)

df['clean_text'] = df['case_text'].apply(clean_text)
print("✅ Text cleaned")

# ── TF-IDF ────────────────────────────────────────────────
vectorizer = TfidfVectorizer(max_features=5000)
tfidf_matrix = vectorizer.fit_transform(df['clean_text'])
print("✅ TF-IDF matrix ready:", tfidf_matrix.shape)

# ── Cosine Similarity ─────────────────────────────────────
def find_similar_cases(query, top_n=5):
    query_vec = vectorizer.transform([clean_text(query)])
    scores = cosine_similarity(query_vec, tfidf_matrix)[0]
    top_indices = scores.argsort()[-top_n:][::-1]
    results = []
    for i in top_indices:
        results.append({
            'case_id'    : df.iloc[i]['case_id'],
            'case_title' : df.iloc[i]['case_title'],
            'case_outcome': df.iloc[i]['case_outcome'],
            'similarity' : round(float(scores[i]), 3)
        })
    return results

# ── Naive Bayes ───────────────────────────────────────────
X = tfidf_matrix
y = df['case_outcome']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

accuracy = nb_model.score(X_test, y_test)
print(f"✅ Naive Bayes trained — Accuracy: {accuracy:.2%}")

def predict_outcome(query):
    query_vec = vectorizer.transform([clean_text(query)])
    prediction = nb_model.predict(query_vec)[0]
    proba = nb_model.predict_proba(query_vec)[0]
    confidence = round(float(max(proba)) * 100, 1)
    return prediction, confidence