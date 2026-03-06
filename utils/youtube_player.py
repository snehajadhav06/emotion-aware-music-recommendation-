from youtubesearchpython import VideosSearch

def get_youtube_video(song, artist):

    query = f"{song} {artist}"

    videos_search = VideosSearch(query, limit=1)

    result = videos_search.result()

    if result["result"]:
        return result["result"][0]["link"]

    return None

