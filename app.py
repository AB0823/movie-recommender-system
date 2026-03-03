import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: white;
    }
    .stButton>button {
        background-color: #E50914;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Recommender")
st.markdown("Find movies you'll love instantly 🚀")


@st.cache_data
def load_data():
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movies_dict = pickle.load(open("movies_dict.pkl", "rb"))
    movies = pd.DataFrame(movies_dict)
    return similarity, movies

similarity, movies = load_data()

def fetch_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    try:
        response = requests.get(url)
        data = response.json()

        poster = (
            "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            if data.get('poster_path')
            else "https://via.placeholder.com/500x750?text=No+Image"
        )

        rating = data.get("vote_average", "N/A")
        rating = round(float(rating), 1)
        year = data.get("release_date", "N/A")[:4]

        return poster, rating, year
    except:
        return "https://via.placeholder.com/500x750?text=Error", "N/A", "N/A"


def recommend(movie_name):
    matches = movies[movies['title'].str.lower().str.contains(movie_name.lower())]

    if matches.empty:
        return []

    movie_index = matches.index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster, rating, year = fetch_details(movie_id)

        recommendations.append({
            "title": title,
            "poster": poster,
            "rating": rating,
            "year": year
        })

    return recommendations


selected_movie = st.selectbox(
    "🔎 Search for a Movie",
    movies['title'].values
)

if st.button("Recommend"):

    if selected_movie.strip() == "":
        st.warning("Please enter a movie name.")
    else:
        with st.spinner("Finding similar movies... 🎥"):
            results = recommend(selected_movie)

        if not results:
            st.error("No matching movie found.")
        else:
            st.markdown("### Top 5 Similar Movies 🍿")
            cols = st.columns(5)

            for idx, movie in enumerate(results):
                with cols[idx]:
                    st.image(movie["poster"])
                    st.markdown(f"**{movie['title']}**")
                    st.markdown(f"⭐ Rating: {movie['rating']}")
                    st.markdown(f"📅 Year: {movie['year']}")