

# 📚 Book Recommendation System Using Content Filtering

An advanced **hybrid book recommendation engine** built with Python and Streamlit, leveraging **content-based filtering, popularity scores, diversity boosting, clustering, and embeddings** for smarter recommendations.

The system allows users to:

* Get **personalized recommendations** for any book.
* Explore by **genre**, **author**, or trending books.
* Understand **why** a recommendation was made.
* View **dataset insights** with interactive visualizations.

---

## 🚀 Features

✅ **Hybrid Recommendation Engine**

* Combines **content similarity, popularity, and diversity**.
* Boosts results with **user preference clusters**.
* Uses **TF-IDF embeddings + SVD dimensionality reduction**.

✅ **Interactive Streamlit Interface**

* Search for books, get recommendations instantly.
* Explore recommendations by **genre** or **author**.
* View **explanations** for each recommended book.
* "🎲 Surprise Me!" feature for random book picks.

✅ **Dataset Insights**

* Genre distribution visualization.
* Popularity scores with Bayesian adjustment.
* Metrics: Average rating, total books, unique genres.

✅ **Evaluation Metrics**

* Precision, Recall, NDCG, Diversity, and Coverage.

---

## 📂 Project Structure

```
.
├── enhanced_recommender.py      # Main implementation (your code)
├── complete_books_dataset.csv   # Dataset (must be provided by user)
├── book_recommender_model.pkl   # Saved model components (auto-created)
└── README.md
```

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/book-recommender.git
cd book-recommender
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📋 requirements.txt

Copy this into a file named **`requirements.txt`**:

```
pandas
numpy
scikit-learn
streamlit
matplotlib
joblib
```

---

## ▶️ Usage

### 1. Run Streamlit Web App

```bash
streamlit run enhanced_recommender.py
```

This will launch the interactive **Book Recommendation Dashboard** in your browser.

### 2. Command-line Demo

```bash
python enhanced_recommender.py
```

This runs backend tests:

* Loads dataset
* Generates sample recommendations
* Prints explanations
* Runs evaluation

---

## 📊 Dataset

* Must be in **CSV format** (default: `complete_books_dataset.csv`).
* **Required column**:

  * `title`
* **Recommended columns** (improves accuracy):

  * `authors`, `genres`, `average_rating`, `description`, `ratings_count`, `tags`

---

## 📖 Example

**Hybrid Recommendation Output:**

| Title  | Authors  | Genres           | Avg Rating | Score |
| ------ | -------- | ---------------- | ---------- | ----- |
| Book A | Author X | Fiction, Mystery | 4.5        | 0.912 |
| Book B | Author Y | Thriller, Drama  | 4.2        | 0.875 |

**Explanation Example:**

```
'Book B' is recommended because:
- Shares genres: Thriller
- Content similarity: 0.78
- Average rating: 4.2/5.0
- Belongs to the same preference cluster
```

---

## 📈 Evaluation Metrics

The system can evaluate itself using a set of test books.
It reports:

* **Precision**
* **Recall**
* **NDCG (ranking quality)**
* **Diversity (genre spread)**
* **Catalog coverage**

---

## 🌟 Future Improvements

* Integrate **collaborative filtering** with user ratings.
* Deploy on cloud (Streamlit Cloud / Hugging Face Spaces).
* Add **real-time user profiles & personalization**.
* Support for multilingual book data.

---

