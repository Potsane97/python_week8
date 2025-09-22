# COVID-19 Metadata Visualisation

This project is a **Streamlit web app** for exploring and visualizing the COVID-19 research metadata from the CORD-19 dataset. It guides users from data loading, cleaning, analysis, and visualization, up to an interactive dashboard.

## Project Overview

The project performs the following steps:

### 1. Data Loading and Basic Exploration

* Download the `metadata.csv` file from the CORD-19 dataset.
* Load it into a pandas DataFrame.
* Examine the first few rows and structure.
* Check DataFrame dimensions (rows, columns) and column data types.
* Identify missing values in important columns.
* Generate basic statistics for numerical columns.

### 2. Data Cleaning and Preparation

* Handle missing data by removing or imputing missing values.
* Drop columns with too many missing values (`mag_id`, `who_covidence_id`, `arxiv_id`, `s2_id`).
* Convert `publish_time` to datetime and extract `publish_year`.
* Create new columns such as `abstract_word_count` and `num_authors`.
* Save the cleaned dataset as `df_cleaned.csv`.

### 3. Data Analysis and Visualization

* Count papers by publication year.
* Identify top journals publishing COVID-19 research.
* Perform basic text analysis (most frequent words in titles).
* Create visualizations:

  * Line chart of publications over time.
  * Bar chart of top publishing journals.
  * Word cloud from paper titles.
* Distribution of paper counts by source.

### 4. Streamlit App

* Interactive dashboard that:

  * Automatically loads the cleaned dataset (`df_cleaned.csv`).
  * Displays dataset preview.
  * Provides visualizations (publications over time, top journals, word cloud).
  * Optional: interactive filters by year and journal.
* Users can also enter their own data via a form and see it displayed in JSON and table formats.
* Uses caching to speed up data loading.

## Installation

Clone the repository:

```
git clone https://github.com/Potsane97/python_week8.git
cd your-repo
```

Install dependencies:

```
pip install -r requirements.txt
```

## Run the App

```
streamlit run app.py
```

## Deployment

1. Push the repository to GitHub.
2. Connect your GitHub repo to [Streamlit Cloud](https://streamlit.io/cloud).
3. Set the entry point as `app.py`.
4. Click **Deploy** to view your dashboard online.

## Project Structure

```
.
├── app.py             # Main Streamlit app
├── df_cleaned.csv     # Cleaned dataset
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Notes

* The dataset used in the app is a cleaned and reduced version of the CORVID-19 metadata to keep the dashboard lightweight.
* The app avoids asking users to upload the full dataset.
* Additional user data input is supported via an interactive form.
