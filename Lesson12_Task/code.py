import pandas as pd

data = pd.read_csv('/content/taylor_album_songs.csv', header=None) # PANDAS detected delimiter automatically
df = pd.DataFrame(data)

df.columns = df.iloc[0] # make row 0 to be column names
df = df[1:].reset_index(drop=True) # move the rest of the data one row upwards

track_count = df.groupby('album_name')['track_name'].count()
print(f'Track count for each of the albums {track_count}')

album = 'Midnights'
filtered_df = df[df['album_name'] == album] # filter data by the album name
print(f'\n{album} tracklist:')
for index, track_name in enumerate(filtered_df['track_name'], start=1): # reassign index starting from 1 to tracknames
  print(f"{index}   {track_name}")

longest_song_index = (pd.to_numeric(df['duration_ms'], errors='coerce')).idxmax() # find index of max length song, while converting the data to numeric values
longest_song = df.loc[longest_song_index, 'track_name'] # finding songname based on index
album_of_longest_song = df.loc[longest_song_index, 'album_name'] # finding album based on the index
longest_song_length = int(df.loc[longest_song_index, 'duration_ms'])/1000/60 # finding length and converting ms to min
print(f'\nThe longest song in the discography is {longest_song} from {album_of_longest_song}, it is {longest_song_length} min')
