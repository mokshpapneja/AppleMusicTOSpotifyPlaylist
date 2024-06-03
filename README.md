# AppleMusicTOSpotifyPlaylist
A python-selenium based code that accesses Spotify API to transfer your apple music playlist(as of now the first 100 songs of it batch to be added later) to a spotify playlist.

Steps:
1. Make a spotify account
2. Go to spotify for developers :https://developer.spotify.com/documentation/web-api/concepts/apps
3. Click Create App and register this under any name using the Web-API with redirect url as : 'http://localhost:8888/callback'
4. You will get the client ID and secret using the above.
5. Download the repo.
6. Make sure you have python3 installed.
7. pip install selenium request spotipy
8. Make sure that chromedriver can open chrome by referring to this. https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de
9. Run the code.
10. Enjoy the first 100 of your playlist from Apple music on your new spotify playlist.


Imp: Will be adding batch support in a while but too sleepy for it.
