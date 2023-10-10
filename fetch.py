import spotipy
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

URL = 'https://api.spotify.com/v1/me/player/currently-playing'
ID = os.getenv("ID") # Get spotify app id from .env file
SECRET = os.getenv("SECRET") # Get spotify app secret from .env file
REDIRECT = os.getenv("REDIRECT") # Get spotify app redirect url from .env file
SCOPE = "user-read-currently-playing" # Initialise scope
# Get max length of an artist name to display from .env file. If it doesn't exist then defaults to 13 characters
MAX_ARTIST_LEN = int(os.getenv("MAX_ARTIST_LEN")) if os.getenv("MAX_ARTIST_LEN") and os.getenv("MAX_ARTIST_LEN") != "" else 39
# Get max length of an song name to display from .env file. If it doesn't exist then defaults to 39 characters
MAX_NAME_LEN = int(os.getenv("MAX_NAME_LEN")) if os.getenv("MAX_NAME_LEN") and os.getenv("MAX_NAME_LEN") != "" else 39

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
            "artists": artist_names
        }
    # If not, return default set of values
    else:
        current_details = {
            "id": None,
            "name": "Not playing",
            "cover": None,
            "artists": "Not playing"
        }
    return current_details