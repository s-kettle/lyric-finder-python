import requests
from requests.exceptions import HTTPError

try:
    artist = input("Enter an artist: ")
    title = input("Enter a song title: ")

    response = requests.get(f'https://api.lyrics.ovh/v1/{artist}/{title}')
    response.raise_for_status()

    json = response.json()

    print(f"Here are the lyrics for {title} by {artist}")
    print(json["lyrics"])


except HTTPError as http_err:
    print(f'The lyrics for {title} by {artist} cannot be found.')
except Exception as e:
    print(f'Other error occurred: {e}')
