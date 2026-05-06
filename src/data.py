import pandas as pd
import ast
import numpy as np
import requests

# -------------------------
# Helper: extract names
# -------------------------
def extract_names(obj):
    try:
        obj = ast.literal_eval(obj)
        return [item['name'] for item in obj]
    except:
        return []


# -------------------------
# Helper: success score
# -------------------------
def compute_success(row):
    budget = row['budget']
    revenue = row['revenue']

    if budget == 0 or revenue == 0:
        return 0

    return revenue / budget


# -------------------------
# Main preprocessing
# -------------------------
def load_and_preprocess():
    movies = pd.read_csv("Data/movies_metadata.csv", low_memory=False)

    movies = movies[[
        "title",
        "overview",
        "genres",
        "original_language",
        "vote_average",
        "budget",
        "revenue",
        "poster_path"
    ]]

    movies = movies.dropna(subset=["title", "overview", "poster_path"])

    movies["budget"] = pd.to_numeric(movies["budget"], errors="coerce").fillna(0)
    movies["revenue"] = pd.to_numeric(movies["revenue"], errors="coerce").fillna(0)

    movies = movies.fillna("")

    movies["genres"] = movies["genres"].apply(extract_names)
    movies["genres"] = movies["genres"].apply(lambda x: " ".join(x)).str.lower()

    movies["overview"] = movies["overview"].str.lower()

    movies["content"] = movies["overview"] + " " + movies["genres"]

    movies["success"] = movies.apply(compute_success, axis=1)
    movies["success"] = np.log1p(movies["success"])

    if movies["success"].max() > 0:
        movies["success"] = (
            (movies["success"] - movies["success"].min()) /
            (movies["success"].max() - movies["success"].min())
        )

    movies["vote_average"] = movies["vote_average"] / 10.0

    movies["poster_url"] = movies["poster_path"].apply(
        lambda x: f"https://image.tmdb.org/t/p/w500{x}" if isinstance(x, str) and x.strip() else ""
    )

    return movies

