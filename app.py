import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'aa4b6b300fdb4797bfe7625e121c99cd'
secret = 'ddbca51759f340e58471ec1b929bad7b'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# "attention" 부분은 track_input으로 수정할 예정입니다.

track_search = sp.search("attention", limit=10, type='track', market=None)

track_results = []
artists_results = []

for track in track_search['tracks']['items']:

    for artist in track['artists']:
        artists_result = artist['name']
        artists_results.append(artists_result)
    track_result = track['name']
    track_results.append(track_result)

print(track_results[0])
print(artists_results[0])

