# recommender_core.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os # To handle relative paths

# --- Data Loading and Preprocessing (from previous phases) ---
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'anime.csv')
anime_df = pd.read_csv(DATA_PATH)

# Handle missing genres
anime_df['genre'] = anime_df['genre'].fillna('')

# Create content features
anime_df['content_features'] = anime_df['genre']

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(anime_df['content_features'])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index mapping
indices = pd.Series(anime_df.index, index=anime_df['name']).drop_duplicates()
# --- End Data Loading and Preprocessing ---

def get_recommendations(title):
    # Pass pre-loaded objects to avoid reloading
    if title not in indices:
        return [] # Return empty list for no recommendations

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11] # Get top 10, excluding itself

    anime_indices = [i[0] for i in sim_scores]
    return anime_df['name'].iloc[anime_indices].tolist() # Return as list
