# Movie Recommender System

An interactive Content-Based Movie Recommendation System built using TF-IDF Vectorization and Cosine Similarity, deployed with Streamlit.
This application recommends 5 similar movies based on the selected movie and displays:
🎥 Movie Posters
⭐ IMDb Rating (rounded to 1 decimal)
📅 Release Year
🔎 Searchable Dropdown Interface
☀️ Clean Light-Themed UI

# Features
  Content-based recommendation using movie metadata
  NLP-based text preprocessing (genres, cast, crew, keywords, overview)
  Vectorization using Bag-of-Words (CountVectorizer)
  Cosine Similarity for ranking similar movies
  TMDB API integration for real-time posters, ratings & release year
  Searchable dropdown UI
  Loading spinner animation
  Error handling for missing posters or invalid selections
  Clean light theme interface

# How It Works
  The Kaggle TMDB 5000 Movies Dataset is cleaned and preprocessed.
  Important textual features are combined into a single tags column.
  Text is vectorized using TF-IDF Vectorizer.
  Cosine similarity is calculated between all movie vectors.
  When a movie is selected:
  Top 5 most similar movies are identified.
  TMDB API fetches poster, rating, and release year.
  Results are displayed in a responsive layout.

#Tech Stack
  Python
  Pandas
  Scikit-learn
  TF-IDF Vectorizer
  Cosine Similarity
  Streamlit
  TMDB API
  Pickle (Model Serialization)
