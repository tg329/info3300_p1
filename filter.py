import pandas as pd

# Load the CSV file (use the correct delimiter)
file_path = 'bestSongs.csv'
df = pd.read_csv(file_path, delimiter=';')

# Filter out songs from before the year 2000
df_filtered = df[df['year'] >= 2000]

# Sort by 'year' and 'popularity', descending order
df_sorted = df_filtered.sort_values(['year', 'popularity'], ascending=[True, False])

# Group by 'year' and take the top 15 songs of each year
top_songs = df_sorted.groupby('year').head(15)

# Save the result to a new CSV file
top_songs.to_csv('top_15_songs_per_year.csv', index=False)
