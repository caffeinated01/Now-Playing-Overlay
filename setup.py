import spotipy
import os
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv("ID") # Get spotify app id from .env file
SECRET = os.getenv("SECRET") # Get spotify app secret from .env file
REDIRECT = os.getenv("REDIRECT") # Get spotify app redirect url from .env file
SCOPE = "user-read-currently-playing" # Initialise scope

oauth = spotipy.SpotifyOAuth(client_id=ID,
                             client_secret=SECRET,
                             redirect_uri=REDIRECT,
                             scope=SCOPE)

oauth.get_access_token()