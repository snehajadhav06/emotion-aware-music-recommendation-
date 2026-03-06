import requests

def get_album_art(song, artist):

    query = f"{song} {artist}".replace(" ", "+")

    url = f"https://itunes.apple.com/search?term={query}&limit=1"

    try:
        response = requests.get(url).json()

        if response["resultCount"] > 0:
            return response["results"][0]["artworkUrl100"]

    except:
        return None

    return None

