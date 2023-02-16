# Create-a-Spotify-Playlist-using-the-Musical-Time-Machine
This project uses web scraping, the Beautiful Soup library, and the Spotify API through the Spotipy library to create a playlist of the top 100 songs for a given year according to the Billboard Hot 100 chart.

The project first prompts the user to enter a year in YYYY-MM-DD format. It then constructs the URL for the corresponding Billboard chart and uses requests to retrieve the HTML content of the page. Beautiful Soup is used to parse the HTML and extract the titles of the top 100 songs, which are stored in a list.

Next, the project uses the Spotify API to authenticate the user and create a new public playlist with a name indicating the year requested by the user. The playlist is initialized with a description, and the ID of the new playlist is stored.

Finally, the project loops through the list of top 100 songs and adds each song to the newly created playlist using the song name to search the Spotify library and retrieve the song's URI. If a song is found, its URI is added to the playlist. If not, an error message is displayed indicating that the song was not found.
