# 🎵 Spotify Catalogue Data Analysis

### A Python-Based Exploratory Data Analysis Project Using Pandas

An interactive, beginner-friendly Python project that analyzes a Spotify catalogue dataset to uncover insights about song popularity, streaming performance, artists, genres, release years, and audio characteristics.

The project uses **Python and Pandas** to perform data exploration, cleaning, filtering, sorting, grouping, and statistical analysis. It also features an interactive command-line interface that allows users to explore the dataset through a simple menu.

---

## 📌 Project Overview

Music streaming platforms generate large amounts of data about songs, artists, and listening trends. Analyzing this data can help us understand patterns in music popularity and streaming performance.

This project explores a Spotify catalogue dataset containing **200 tracks and 33 columns**. It focuses on extracting meaningful information through Python-based data analysis.

The program generates a detailed text report and provides an interactive menu for exploring different aspects of the dataset.

## 🎯 Project Objectives

- Analyze song popularity and streaming performance.
- Identify the most popular and most-streamed tracks.
- Explore artist contributions and streaming statistics.
- Understand genre distribution and popularity.
- Examine music trends across different release years.
- Analyze audio characteristics such as danceability, energy, loudness, and tempo.
- Apply fundamental Python programming and data analysis concepts.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Pandas | Data manipulation and analysis |
| CSV | Dataset storage format |
| VS Code / Terminal | Development and execution |

## 📂 Dataset Information

**Dataset:** `spotify_catalogue.csv`

| Attribute | Details |
|---|---|
| Total Records | 200 |
| Total Columns | 33 |
| Data Format | CSV |
| Records Analyzed | First 200 rows |
| Main Library | Pandas |

**Important Dataset Columns:**

- `track_name` – Name of the song.
- `artist_name` – Name of the artist.
- `album_name` – Album containing the track.
- `genre` – Music genre.
- `country` – Country information.
- `release_year` – Year of release.
- `popularity` – Track popularity score.
- `stream_count` – Number of streams recorded.
- `duration_minutes` – Track duration.
- `danceability` – Danceability score.
- `energy` – Energy level.
- `loudness` – Loudness measurement.
- `tempo` – Track tempo.

## ✨ Key Features

### 1. Data Overview
- Total number of tracks.
- Unique artists and genres.
- Release date range.
- Missing values and duplicate records.
- Dataset preview.

### 2. Song Popularity Analysis
- Top 10 most popular tracks.
- Top 10 tracks by streaming count.
- Average popularity score.
- Identification of the most popular song.

### 3. Artist Analysis
- Artists with the highest number of tracks.
- Artists with the highest total streams.
- Comparison of artist contributions.

### 4. Genre Analysis
- Number of tracks in each genre.
- Genre-wise percentage distribution.
- Average popularity by genre.

### 5. Release Year Analysis
- Number of tracks released each year.
- Average popularity by release year.
- Median streaming count.
- Identification of the year with the most tracks.

### 6. Audio Features Analysis
- Average danceability.
- Average energy.
- Average loudness.
- Average tempo.
- Explicit and non-explicit track comparison.
- Correlation between audio features and popularity.

### 7. Key Findings
Generates a summary of important observations obtained from the dataset.

### 8. Interactive Command-Line Menu
Users can interact with the dataset through a menu-driven interface without modifying the Python code.

## 💻 Interactive Menu

| Option | Functionality |
|:---:|---|
| 1 | Show total songs |
| 2 | Show total streams |
| 3 | Show average popularity |
| 4 | Show the most popular song |
| 5 | Search for a song |
| 6 | Search for an artist |
| 7 | Explore songs by genre |
| 8 | Explore songs by release year |
| 9 | Display the complete analysis report |
| 0 | Exit the program |

## 📁 Project Structure

```text
Spotify-Catalogue-Data-Analysis/
│
├── spotify_analysis_200.py
│
├── spotify_catalogue.csv
│
└── README.md
```

## ⚙️ Installation & Setup

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Install Pandas

Open Terminal and execute:

```bash
python3 -m pip install pandas
```

### Step 3: Download or Clone the Repository

```bash
git clone https://github.com/anujpratap4242/Spotify-Catalogue-Data-Analysis.git
```

### Step 4: Open the Project Folder

```bash
cd Spotify-Catalogue-Data-Analysis
```

### Step 5: Run the Program

```bash
python3 spotify_analysis_200.py
```

### Step 6: Generate the Complete Report

```bash
python3 spotify_analysis_200.py --report
```

**Note:** Keep the Python script and CSV file in the same directory. The dataset must be named `spotify_catalogue.csv` to match the filename expected by the code.

## 🧠 Python Concepts Demonstrated

This project demonstrates the practical application of the following concepts:

- Variables and data types.
- Conditional statements and loops.
- Functions and modular programming.
- File handling and CSV reading.
- Pandas DataFrames and Series.
- Data cleaning and preprocessing.
- Data filtering and selection.
- Sorting and grouping operations.
- Statistical calculations and aggregation.
- Missing-value handling.
- Duplicate detection.
- Correlation analysis.
- Command-line user interaction.

**Important Pandas Functions Used:**

| Function | Purpose |
|---|---|
| `pd.read_csv()` | Loads CSV data |
| `head()` | Displays the first rows |
| `info()` | Shows dataset information |
| `describe()` | Generates statistical summaries |
| `isnull()` | Identifies missing values |
| `drop_duplicates()` | Removes duplicate records |
| `groupby()` | Groups records by categories |
| `sort_values()` | Sorts records |
| `value_counts()` | Counts category occurrences |
| `mean()` | Calculates average |
| `median()` | Calculates median |
| `sum()` | Calculates total |
| `nunique()` | Counts unique values |
| `corr()` | Calculates correlations |

## ⚠️ Project Limitations

- The analysis is limited to the first 200 rows.
- Results depend entirely on the supplied CSV dataset.
- The project does not fetch real-time data from Spotify.
- Correlation does not imply causation.
- The current version generates terminal-based reports rather than graphical dashboards.

## 🚀 Future Improvements

The project can be extended with the following features:

- Add data visualizations using Matplotlib and Seaborn.
- Develop an interactive dashboard using Streamlit.
- Integrate the Spotify Web API for updated music information.
- Allow users to select the number of records for analysis.
- Introduce advanced filtering and comparative analysis.
- Expand the dataset to include more tracks and artists.

## 👨‍💻 Author

**Anuj Pratap Singh**

B.Tech – Computer Science and Engineering

**Project Type:** Academic / Beginner-Level Data Analysis Project

**Domain:** Python Programming | Data Analytics

---

*This project was developed for educational purposes to demonstrate the fundamentals of Python programming and exploratory data analysis using Pandas.*