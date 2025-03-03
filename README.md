# Book Recommendation System using Content Filtering

## Overview
This project is a **Book Recommendation System** that uses **Content-Based Filtering** to suggest books similar to a given title. The system is built using **Python, Tkinter (GUI), Pandas, Scikit-learn, and SciPy**. It calculates book similarity using **TF-IDF (for descriptions), MultiLabelBinarizer (for genres & tags), and Cosine Similarity**.

## Features
- **User-friendly GUI** built with Tkinter.
- **Search for a book** by entering its title.
- **Recommends similar books** based on content filtering.
- **Displays details** including title, authors, genres, tags, average rating, and similarity score.

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed and install the required dependencies:

```sh
pip install pandas scikit-learn scipy tkinter
```

### Dataset
- Ensure you have a CSV dataset (`complete_books_dataset.csv`) containing columns like `title`, `authors`, `genres`, `tags`, `description`, and `average_rating`.

## Running the Application
1. Clone or download this repository.
2. Make sure the dataset is in the same directory.
3. Run the Python script:
   ```sh
   python app.py
   ```

## How It Works
1. **Preprocessing**:
   - Converts `genres` and `tags` to lowercase and strips whitespace.
   - Uses **MultiLabelBinarizer** to encode `genres` and `tags`.
   - Applies **TF-IDF Vectorization** on `description`.
   - Combines weighted features to compute **Cosine Similarity**.

2. **Recommendation Algorithm**:
   - Finds the index of the searched book.
   - Computes similarity scores with all books.
   - Returns the top 5 most similar books.

3. **GUI Implementation**:
   - Users enter a book title and click "Get Recommendations".
   - Recommended books are displayed in the Tkinter window.

## Example Usage
### Input:
```
Book Title: The Great Gatsby
```

### Output:
```
1. Title: This Side of Paradise
   Authors: F. Scott Fitzgerald
   Genres: fiction, classic
   Tags: romance, historical
   Average Rating: 4.2
   Similarity Score: 0.87

2. Title: Tender is the Night
   Authors: F. Scott Fitzgerald
   Genres: fiction, drama
   Tags: romance, psychological
   Average Rating: 4.0
   Similarity Score: 0.85
```

## Known Issues
- **Title Sensitivity**: The search requires an exact match (case-insensitive).
- **Dataset Dependency**: Ensure the dataset includes relevant books.

## Future Improvements
- Implement fuzzy matching for book titles.
- Allow filtering by user preferences (e.g., only fiction books).
- Improve GUI aesthetics.

## Contributing
Feel free to submit issues or enhancements via pull requests.

## License
This project is open-source and available under the MIT License.
