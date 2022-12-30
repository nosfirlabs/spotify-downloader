import spotipy
import spotipy.util as util

# Replace these with your own client ID and client secret
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"

# Set the redirect URI for your application
redirect_uri = "http://localhost:8888/callback"

# Set the scope for the permissions your application will need
# In this example, we are requesting the ability to read a user's playlists
scope = "user-read-private"

# Get the authorization token
token = util.prompt_for_user_token(
    username, scope, client_id, client_secret, redirect_uri
)

# Create a Spotify client using the authorization token
sp = spotipy.Spotify(auth=token)

# Set the track ID for the track you want to download
track_id = "YOUR_TRACK_ID"

# Get the track's streaming URL
track_info = sp.track(track_id)
stream_url = track_info["preview_url"]

# Download the track
import urllib.request

urllib.request.urlretrieve(stream_url, "track.mp3")
