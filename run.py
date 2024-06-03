#Moksh Papneja
#
#Copyright by @mokshpapneja
#
#Done yet only for the first 100 songs because I am sleepy will add batch updates when next free and motivated



import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(executable_path='chromedriver-mac/chromedriver')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
import string
import json

print(selenium.__version__)
# URL of the page to open
url = 'https://music.apple.com/in/playlist/punjabi-pop/pl.u-EdAVkGGFDmZKeea'  # Replace this URL with the desired page URL

# Open the URL
driver.get(url)
time.sleep(2)
songsDivs = driver.find_elements(By.CLASS_NAME,'songs-list-row.drop-reset.svelte-yw8vjw.songs-list-row--artwork.songs-list-row--two-lines.songs-list-row--playlist.songs-list-row--preview')
songNames=[]
for sD in songsDivs:
    sD=sD.text[:-5]
    s=sD.split("\n")
    print(s)
    songNames.append(s)
    
time.sleep(2)
print(songNames)
appleTracks=[]
for name in songNames:
    appleTracks.append(name[0]+" "+name[1])
#-----------------------------------------------
# Configuration for Spotify
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
spotify_client_id = '------Enter Spotify Client ID by Making a spotify account as developer--------'
spotify_client_secret = '---------Register this app by any name and get Client secret-----------'
spotify_redirect_uri = 'http://localhost:8888/callback'

# Set up Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=spotify_redirect_uri,
                                               scope="playlist-modify-public playlist-modify-private"))

# Function to create Spotify playlist and add tracks
def create_spotify_playlist(playlist_name, track_uris):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, playlist_name)
    sp.user_playlist_add_tracks(user_id, playlist['id'], track_uris)

# Convert Apple Music tracks to Spotify track URIs
def convert_tracks_to_spotify_uris(tracks):
    spotify_uris = []
    for track in tracks:
        print(1)
        results = sp.search(q=track, type='track', limit=1)
        print(1)
        print(results)
        if results['tracks']['items']:
            spotify_uris.append(results['tracks']['items'][0]['uri'])
    return spotify_uris

# Main function to transfer playlist
def transfer_playlist(appleTracks):
    
    spotify_uris = convert_tracks_to_spotify_uris(appleTracks)

    create_spotify_playlist("My Imported Playlist", spotify_uris[0:100])

# Run the transfer
transfer_playlist(appleTracks)
