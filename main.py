from bs4 import BeautifulSoup
import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

username = "317ml6rwafvezerzgxs4jsamfl2i"
scope = "playlist-modify-public"
client_id = "9da2bb5a5f88476a91f7e29c8134dc45"
client_secret = "bb51b4a2628546678f2d0c931d9c9e21"
redirect_uri = "http://mysite.com/callback/"
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














#import requests
#from bs4 import BeautifulSoup
##date = input("please enter a date  in this format YYYY-MM-DD:")
#date = "2022-08-12"
#response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
#top_song_url= response.text
#soup = BeautifulSoup(top_song_url, "html.parser")
##print(soup.prettify())
#table_results = soup.find(class_= 'chart-results // lrv-a-wrapper lrv-u-padding-lr-00@mobile-max')
#songs_tags = table_results.find_all(id='title-of-a-story', name='h3', class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
#songs_list = []
##print(songs_tags)
#for song in songs_tags:
#    clear_text = song.text.replace('\n', '').replace('\t', '')
#    songs_list.append(clear_text)
#print(songs_list)
