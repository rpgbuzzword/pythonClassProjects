import requests
import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from billboardScraper import BillboardScraper

load_dotenv("keys.env")
#Initialize spotipy object, using the Oauth init function at the following url: https://spotipy.readthedocs.io/en/2.13.0/#module-spotipy.oauth2
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="https://example.com",
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_SECRET"),
    cache_path=".cache-Spencer Cumming"
    ))

# 
# 
#Create a BillboardScraper object, get requested date from user with get_Date(), and then
#populating its self.billboardArtists and self.billboardSongs fields with the response from timeTravel()
bs = BillboardScraper()
bs.get_Date()
bs.timeTravel(bs.date)


song_uris = []
year = bs.date.split("-")[0]
for song in bs.billboardSongs:

    #Search function from: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.search
    #And using the q parameter as defined: https://developer.spotify.com/documentation/web-api/reference/search
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")



user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user = user_id, name = f"Time Machine Playlist ({bs.date})", public = False)
sp.playlist_add_items(playlist_id=playlist["id"], items = song_uris)