from bs4 import BeautifulSoup
import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

username = "PUTYOURS"
scope = "playlist-modify-public"
client_id = "PUTYOURS"
client_secret = "PUTYOURS"
redirect_uri = "PUTYOURS"
# Assignment 1
# ask the user what year we are going to scrape from
year_requested = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD:")
url = "https://www.billboard.com/charts/hot-100/" + year_requested

def get_song_uri(song_name):
    results = sp.search(song_name, type='track', limit=1)
    items = results['tracks']['items']
    if len(items) > 0:
        return items[0]['uri']
    else:
        return None


#get the site contents based on input date and store as text
response = requests.get(url=url)
contents = response.text
# print(contents)

#make soup from site contents
soup = BeautifulSoup(contents, "html.parser")

#extract the top 100 song titles and put them in a list
top100 = []
titles = []
# check site in edge or chrome dev tools to see fields
titles = soup.find_all(name="h3", class_="a-no-trucate")
top100 = [title.getText().strip() for title in titles]
print(top100)

token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

sp = spotipy.Spotify(auth=token)

# Create a playlist
playlist_name = f"top 100 songs of{year_requested}"
playlist_description = "A playlist created with Spotipy"

playlist = sp.user_playlist_create(username, playlist_name, public=True, description=playlist_description)
playlist_id = playlist["id"]

print(f"Playlist created: {playlist_name} ({playlist_id})")


# Add a song to a playlist
for song in top100:
    song_uri = get_song_uri(song)
    if song_uri:
        print("The URI of the song is:", song_uri)
    else:
        print("No song found with the name 'song name'")
    sp.user_playlist_add_tracks(username, playlist_id, [song_uri])

    print(f"Song added to playlist: {playlist_id}")
