import requests
from requests.exceptions import HTTPError

try:
    # Retrieve artist and song title information from user
    artist = input("Enter an artist: ")
    title = input("Enter a song title: ")

    # Get a response from the lyrics.ovh API
    response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
    response.raise_for_status()

    # Parse the response to JSON
    json = response.json()

    # Print the lyrics to the console
    print(f"Here are the lyrics for {title} by {artist}")
    print(json["lyrics"])


except HTTPError as http_err:
    print(f'The lyrics for {title} by {artist} cannot be found.')
except Exception as e:
    print(f'Other error occurred: {e}')
