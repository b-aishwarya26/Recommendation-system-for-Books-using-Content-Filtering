import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
import scipy.sparse as sp

# Load the dataset (ensure the correct path)
file_path = "complete_books_dataset.csv"  # Change to your actual file path
df = pd.read_csv(file_path)

# Preprocessing steps
df['genres'] = df['genres'].str.lower().str.strip()
df['tags'] = df['tags'].str.lower().str.strip()

mlb_genres = MultiLabelBinarizer()
genres_encoded = mlb_genres.fit_transform(df['genres'].str.split(', '))

mlb_tags = MultiLabelBinarizer()
tags_encoded = mlb_tags.fit_transform(df['tags'].str.split(', '))

tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
descriptions_tfidf = tfidf_vectorizer.fit_transform(df['description'].fillna(''))

genres_weight = 0.4
tags_weight = 0.3
descriptions_weight = 0.3

combined_features = sp.hstack([
    genres_weight * sp.csr_matrix(genres_encoded),
    tags_weight * sp.csr_matrix(tags_encoded),
    descriptions_weight * descriptions_tfidf
])

similarity_matrix = cosine_similarity(combined_features)

def recommend_books(title, df, similarity_matrix, top_n=5):
    idx = df[df['title'].str.lower() == title.lower()].index
    if len(idx) == 0:
        return None  # No book found
    idx = idx[0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
    
    recommendations = [
        {
            "title": df.iloc[i]['title'],
            "authors": df.iloc[i]['authors'],
            "genres": df.iloc[i]['genres'],
            "tags": df.iloc[i]['tags'],
            "average_rating": df.iloc[i]['average_rating'],
            "similarity_score": score
        }
        for i, score in sorted_scores
    ]
    return recommendations

# GUI Code
def display_recommendations(recommendations):
    if recommendations is None:
        messagebox.showerror("Error", "No book found with that title!")
        return
    result_text = ""
    for idx, book in enumerate(recommendations, start=1):
        result_text += f"{idx}. Title: {book['title']}\n"
        result_text += f"   Authors: {book['authors']}\n"
        result_text += f"   Genres: {book['genres']}\n"
        result_text += f"   Tags: {book['tags']}\n"
        result_text += f"   Average Rating: {book['average_rating']}\n"
        result_text += f"   Similarity Score: {book['similarity_score']:.4f}\n\n"
    
    # Display result in the Text widget
    result_display.config(state=tk.NORMAL)
    result_display.delete(1.0, tk.END)
    result_display.insert(tk.END, result_text)
    result_display.config(state=tk.DISABLED)

def on_search_button_click():
    title = title_entry.get()
    if title:
        recommendations = recommend_books(title, df, similarity_matrix)
        display_recommendations(recommendations)
    else:
        messagebox.showerror("Input Error", "Please enter a book title.")

# Create the main window
root = tk.Tk()
root.title("Book Recommendation System")

# Title input label and entry
title_label = tk.Label(root, text="Enter Book Title:")
title_label.pack(pady=5)

title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=5)

# Search button
search_button = tk.Button(root, text="Get Recommendations", command=on_search_button_click)
search_button.pack(pady=10)

# Result display area (Text widget)
result_display = tk.Text(root, width=80, height=15, wrap=tk.WORD, state=tk.DISABLED)
result_display.pack(padx=10, pady=10)

# Start the GUI
root.mainloop()
