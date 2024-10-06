import pandas as pd

file_path = 'bestSongs.csv'
df = pd.read_csv(file_path, delimiter=';')

df_filtered = df[df['year'] >= 2000]
df_sorted = df_filtered.sort_values(['year', 'popularity'], ascending=[True, False])
top_songs = df_sorted.groupby('year').head(15)

top_songs.to_csv('top_15_songs_per_year.csv', index=False)
