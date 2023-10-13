import spotipy
import os
from dotenv import load_dotenv
import json

load_dotenv()

URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ID = os.getenv("ID") # Get spotify app id from .env file
SECRET = os.getenv("SECRET") # Get spotify app secret from .env file
REDIRECT = os.getenv("REDIRECT") # Get spotify app redirect url from .env file
SCOPE = "user-read-currently-playing" # Initialise scope

c = open('config.json')
CONFIG = json.load(c)
# Get max length of an artist name to display from .env file.
MAX_ARTIST_LEN = CONFIG['MAX_ARTIST_LEN']
# Get max length of an song name to display from .env file.
MAX_NAME_LEN =  CONFIG['MAX_NAME_LEN']

# Get all frontend configs
ARTIST_COLOR = CONFIG["ARTIST_COLOR"]
TITLE_COLOR = CONFIG["TITLE_COLOR"]
BACKGROUND_COLOR = CONFIG["BACKGROUND_COLOR"]
WIDTH = CONFIG["WIDTH"]
FLIP = CONFIG["FLIP"]

# Initialise oauth
oauth = spotipy.SpotifyOAuth(client_id=ID,
                             client_secret=SECRET,
                             redirect_uri=REDIRECT,
                             scope=SCOPE)

token = None

def fetch():
    # Get token
    token = oauth.get_cached_token()["access_token"]
    spotify = spotipy.Spotify(auth=token)
    
    # Fetch details of song currently playing
    current = spotify.currently_playing()
    # current = json.loads(json.dumps(c, sort_keys=False, indent=4))

    # Get song id, name, cover, and artist(s) info from spotify
    # Only returns song details if a - spotify is open on client side and b - song is not paused
    if current != None and current['is_playing'] == True:
        song_id = current['item']['id']
        song_name = current['item']['name'][:MAX_NAME_LEN] + "..." if len(current['item']['name']) > MAX_NAME_LEN else current['item']['name']
        song_cover = current['item']['album']['images'][0]['url']
        artists = [artist for artist in current['item']['artists']]
        # Join all the artist names into one string and slice up to 13 characters and ellipsis so artist name does not overflow
        artist_names = artist_names = ', '.join([artist['name'] for artist in artists])[:MAX_ARTIST_LEN] + "..." if len(', '.join([artist['name'] for artist in artists])) > MAX_ARTIST_LEN else ', '.join([artist['name'] for artist in artists])

        current_details = {
            "id": song_id,
            "name": song_name,
            "cover": song_cover,
            "artists": artist_names,
        }
    # If not, return default set of values
    else:
        current_details = {
            "id": None,
            "name": "Not playing",
            "cover": None,
            "artists": "Not playing",
        }
    return current_details

def return_frontend_config():
    frontend_config = {
        "artist_color": ARTIST_COLOR,
        "title_color": TITLE_COLOR,
        "background_color": BACKGROUND_COLOR,
        "width": WIDTH,
        "flip": FLIP
    }
    return frontend_config