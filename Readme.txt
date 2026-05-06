# 🎬 Movie Recommendation System

A modern **AI-powered movie recommendation system** built with **Python** and **Streamlit**, featuring a clean cinematic UI and intelligent hybrid scoring.

---

## 🚀 Features

* 🎯 Content-based recommendation (TF-IDF + KNN)
* ⭐ Hybrid scoring system:

  * 70% similarity
  * 20% rating
  * 10% success (revenue/budget)
* 🎞️ Movie posters from TMDB
* ⚡ Fast and interactive Streamlit interface
* 🎨 Netflix-inspired UI design

---

## 🖼️ Demo

![App Screenshot](screenshot.png)

---

## 🧠 How It Works

1. **Data preprocessing**

   * Clean movie dataset
   * Extract genres
   * Build textual content (overview + genres)

2. **Vectorization**

   * TF-IDF on movie content

3. **Model**

   * K-Nearest Neighbors (KNN)

4. **Scoring**

   * Combine similarity, rating, and success

---

## 📂 Project Structure

```
Movie_Recommender/
│
├── app.py                 # Streamlit frontend
├── Data/
│   └── movies_metadata.csv
├── src/
│   ├── data.py            # Data preprocessing
│   ├── models.py          # Model building (TF-IDF + KNN)
│   └── recommender.py     # Recommendation logic
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sifeddineftoumi/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies

```bash
pip install streamlit pandas numpy scikit-learn
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

## 📊 Dataset

This project uses the **TMDB Movies Dataset**.

Download it from:
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

Place the file here:

```
Data/movies_metadata.csv
```

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎨
* Pandas & NumPy 📊
* Scikit-learn 🤖

---

## 💡 Future Improvements

* 🎬 Netflix-style grid layout
* 🔍 Advanced filtering (genre, language)
* 📈 Popularity-based recommendations
* 🌐 Deploy online (Streamlit Cloud / Render)

---

## 👤 Author

**Toumi Sif Eddine**
**Zakaria Louaddi**
**Mohammed SAdak Al Akrame**

* GitHub: https://github.com/your-username

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
