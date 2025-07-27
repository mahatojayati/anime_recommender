# Anime Recommendation System (Content-Based)

## Project Overview

This project develops a content-based anime recommendation system designed to suggest new anime to users based on their preferences for existing anime. The system analyzes anime content (primarily genres) to identify similarities and provides recommendations for titles that align with a user's stated interests.

The project is structured into two main components:
1.  **Core Recommendation Engine (CLI-based):** A Python backend that processes anime data and calculates similarities to generate recommendations.

## Features

* **Content-Based Filtering:** Recommends anime based on shared genres and themes.
* **TF-IDF Vectorization:** Utilizes TF-IDF to convert anime genre information into numerical vectors for similarity calculation.
* **Cosine Similarity:** Employs cosine similarity to measure the likeness between anime titles.
* **Command-Line Interface (CLI):** Provides a basic text-based interface for testing and direct interaction.
* **Web Interface (Flask):** Offers a user-friendly web page for inputting anime titles and viewing recommendations.

## Technologies Used

* **Python 3.x**
* **Pandas:** For data loading, manipulation, and cleaning.
* **NumPy:** For numerical operations, especially with vector and matrix calculations.
* **Scikit-learn:** For `TfidfVectorizer` and `cosine_similarity`.

## Dataset

This project utilizes the "Anime Recommendations Database" dataset, commonly found on Kaggle.
* **`anime.csv`**: Contains information about various anime titles, including `anime_id`, `name`, `genre`, `type`, `episodes`, `rating`, and `members`. For this content-based system, the `name` and `genre` columns are primarily used.

## Project Structure

anime_recommender/
├── data/
│   └── anime.csv              # Downloaded dataset file
├── recommender_core.py        # Core recommendation logic (data processing, similarity calculation, get_recommendations function)
├── app.py                     # Flask web application entry point
├── requirements.txt           # List of Python dependencies
└── README.md                  # This README file

## Setup and Installation

Follow these steps to set up and run the project locally:

1.  **Clone the Repository (or create the project structure):**
    ```bash
    git clone [https://github.com/your-username/anime-recommender.git](https://github.com/your-username/anime-recommender.git)
    cd anime-recommender
    ```
    *(If not using Git, create the folder structure manually as shown above.)*

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you haven't created `requirements.txt` yet, run `pip install pandas numpy scikit-learn Flask` and then `pip freeze > requirements.txt`)*

5.  **Download the Dataset:**
    * Go to the [Anime Recommendations Database on Kaggle](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database).
    * Download the `anime.csv` file.
    * Create a `data/` directory inside your `anime_recommender/` project folder.
    * Place `anime.csv` inside the `data/` directory.

## How to Run

### 1. Run the Core CLI-based Recommendation Engine (for testing)

You can test the `recommender_core.py` directly (though `app.py` will also import and run it). This is more for verifying the backend logic in isolation.

```bash
python recommender_core.py
(Note: recommender_core.py by itself won't have an interactive output unless you add print statements for testing within it. It's primarily designed to be imported by app.py.)
