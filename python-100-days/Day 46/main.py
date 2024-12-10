import os
import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ['APP_ID'],
                                               client_secret=os.environ['APP_SECRET'],
                                               redirect_uri=os.environ['APP_REDIRECT_URL'],
                                               scope="playlist-modify-public"))


year = input("Enter the year you want to travel to in YYYY-MM-DD format: ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"

response = requests.get(URL)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "html.parser")
list_elem = soup.select('li.o-chart-results-list__item h3#title-of-a-story')
title_labels = [elem.parent for elem in list_elem]

spotify_tracks_to_add = []

for label in title_labels:
    song = label.h3.text.strip()
    author = label.span.text.strip()
    query_result = sp.search(q=f"{song}+{author}")
    spotify_track_url = query_result["tracks"]["items"][0]["external_urls"]["spotify"]
    spotify_tracks_to_add.append(spotify_track_url)
    print(f"Song {song} - {author} added")

spotify_playlist_create_response = sp.user_playlist_create(user=sp.current_user()["id"], name=f'Popular tracks in {year}')
sp.playlist_add_items(playlist_id=spotify_playlist_create_response["id"], items=spotify_tracks_to_add, position=None)
print(f"{len(spotify_tracks_to_add)} tracks added")