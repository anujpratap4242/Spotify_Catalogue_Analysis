"""
Spotify Catalogue Analysis (first 200 songs only)

Files needed in the SAME folder: this file + spotify_catalogue.csv
Library needed: pandas
How to run: python spotify_analysis_200.py            (menu)
            python spotify_analysis_200.py --report   (full report only)
"""

import sys
import pandas as pd

# ---------------------------------------------------------
# 1. Load the data (we only use the first 200 rows)
# ---------------------------------------------------------
df = pd.read_csv("spotify_catalogue.csv")
df = df.head(200)

# ---------------------------------------------------------
# 2. Clean the data
# ---------------------------------------------------------
# remove extra spaces in the text columns
for col in ["track_name", "artist_name", "album_name", "genre", "country", "label"]:
    df[col] = df[col].str.strip()

# change release_date from text to a real date
df["release_date"] = pd.to_datetime(df["release_date"])

# month name column for month wise questions
df["Month"] = df["release_date"].dt.month_name()

# these main numbers are calculated BEFORE the menu so every option can use them
total_songs = len(df)
total_artists = df["artist_name"].nunique()
total_genres = df["genre"].nunique()
total_streams = df["stream_count"].sum()
average_popularity = df["popularity"].mean()
average_duration = df["duration_minutes"].mean()

show_cols = ["track_name", "artist_name", "genre", "release_year", "popularity", "stream_count"]


# ---------------------------------------------------------
# 3. Functions for the full report
# ---------------------------------------------------------
def heading(title):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


def data_overview():
    heading("1. DATA OVERVIEW")
    print("Total songs       :", total_songs)
    print("Total artists     :", total_artists)
    print("Total genres      :", total_genres)
    print("Release dates     :", df["release_date"].min().date(), "to", df["release_date"].max().date())
    print("Missing values    :", df.isnull().sum().sum())
    print("Duplicate rows    :", df.duplicated().sum())
    print("\nFirst 5 rows:")
    print(df[show_cols].head().to_string(index=False))


def top_songs():
    heading("2. TOP 10 SONGS")
    print("By popularity:")
    print(df.sort_values("popularity", ascending=False).head(10)[show_cols].to_string(index=False))
    print("\nBy streams:")
    print(df.sort_values("stream_count", ascending=False).head(10)[show_cols].to_string(index=False))


def artist_report():
    heading("3. ARTISTS")
    table = df.groupby("artist_name").agg(
        songs=("track_id", "count"),
        total_streams=("stream_count", "sum"),
        avg_popularity=("popularity", "mean"),
    )
    table["avg_popularity"] = table["avg_popularity"].round(1)
    print("Top 10 artists by number of songs:")
    print(table.sort_values("songs", ascending=False).head(10))
    print("\nTop 10 artists by total streams:")
    print(table.sort_values("total_streams", ascending=False).head(10))


def genre_report():
    heading("4. GENRES")
    table = df["genre"].value_counts().to_frame("songs")
    table["share_%"] = (table["songs"] / total_songs * 100).round(1)
    print(table)

    print("\nAverage popularity by genre (top 5):")
    print(df.groupby("genre")["popularity"].mean().round(1).sort_values(ascending=False).head(5))


def year_report():
    heading("5. YEAR WISE SUMMARY")
    table = df.groupby("release_year").agg(
        songs=("track_id", "count"),
        avg_popularity=("popularity", "mean"),
        median_streams=("stream_count", "median"),
    )
    table["avg_popularity"] = table["avg_popularity"].round(1)
    print(table)
    print("\nYear with most songs:", table["songs"].idxmax())


def audio_report():
    heading("6. MUSIC FEATURES")
    cols = ["danceability", "energy", "loudness", "tempo"]
    print("Average of each feature:")
    print(df[cols].mean().round(2))

    print("\nExplicit vs not explicit (average):")
    print(df.groupby("explicit")[["popularity", "stream_count"]].mean().round(1))

    print("\nCorrelation with popularity:")
    print(df[cols + ["log_stream_count", "duration_minutes"]].corrwith(df["popularity"]).round(3))


def key_findings():
    heading("7. KEY FINDINGS")
    top_song = df.loc[df["stream_count"].idxmax()]
    print("1. The data has", total_songs, "songs by", total_artists, "artists in", total_genres, "genres")
    print("2. Most streamed song:", top_song["track_name"], "by", top_song["artist_name"],
          "(", top_song["stream_count"], "streams )")
    print("3. Artist with most songs:", df["artist_name"].value_counts().index[0],
          "(", df["artist_name"].value_counts().iloc[0], "songs )")
    print("4. Most common genre:", df["genre"].value_counts().index[0])
    print("5. Average popularity is", round(average_popularity, 1), "and average song length is",
          round(average_duration, 2), "minutes")
    print("6. Average streams is", round(df["stream_count"].mean()), "but the median is",
          df["stream_count"].median(), "(a few big hits pull the average up)")


def full_report():
    data_overview()
    top_songs()
    artist_report()
    genre_report()
    year_report()
    audio_report()
    key_findings()


# ---------------------------------------------------------
# 4. The menu
# ---------------------------------------------------------
def run_menu():
    while True:
        print("\n===== SPOTIFY CATALOGUE EXPLORER =====")
        print("1. Total Songs")
        print("2. Total Streams")
        print("3. Average Popularity")
        print("4. Most Popular Song")
        print("5. Search Song by Name")
        print("6. Search Artist")
        print("7. Genre Wise Songs")
        print("8. Songs of a Year")
        print("9. Full Report")
        print("0. Exit")

        choice = input("\nWhat do you want to know? Enter 0-9: ").strip()

        if choice == "1":
            print("Total songs in the data are:", total_songs)

        elif choice == "2":
            print("Total streams are:", total_streams)

        elif choice == "3":
            print("Average popularity is:", round(average_popularity, 2))

        elif choice == "4":
            best = df.sort_values(["popularity", "stream_count"], ascending=False).iloc[0]
            print("Most popular song is:", best["track_name"], "by", best["artist_name"],
                  "- popularity", best["popularity"])

        elif choice == "5":
            name = input("Enter song name (or part of it): ").strip()
            found = df[df["track_name"].str.contains(name, case=False, regex=False)]
            if name == "" or found.empty:
                print("No song found for", name)
            else:
                print("Found", len(found), "song(s):")
                print(found.sort_values("popularity", ascending=False).head(10)[show_cols].to_string(index=False))

        elif choice == "6":
            name = input("Enter artist name (or part of it): ").strip()
            found = df[df["artist_name"].str.contains(name, case=False, regex=False)]
            if name == "" or found.empty:
                print("No artist found for", name)
            else:
                print("Found", found["artist_name"].nunique(), "artist(s) with", len(found), "song(s):")
                print(found.sort_values("popularity", ascending=False).head(10)[show_cols].to_string(index=False))

        elif choice == "7":
            print("Genres:", ", ".join(sorted(df["genre"].unique())))
            genre_name = input("Enter genre name: ").strip()
            found = df[df["genre"].str.lower() == genre_name.lower()]
            if found.empty:
                print("Genre not found. Choose one from the list above.")
            else:
                print(len(found), "song(s) in", genre_name, "- top 5 by popularity:")
                print(found.sort_values("popularity", ascending=False).head(5)[show_cols].to_string(index=False))

        elif choice == "8":
            year_text = input("Enter year (2020-2025): ").strip()
            if not year_text.isdigit() or int(year_text) not in df["release_year"].values:
                print("No songs found for that year.")
            else:
                found = df[df["release_year"] == int(year_text)]
                print(len(found), "song(s) released in", year_text, "- top 5 by popularity:")
                print(found.sort_values("popularity", ascending=False).head(5)[show_cols].to_string(index=False))

        elif choice == "9":
            full_report()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


# ---------------------------------------------------------
# 5. Start the program
# ---------------------------------------------------------
if "--report" in sys.argv:
    full_report()      # prints the whole report and stops
else:
    run_menu()
