import pandas as pd
import random
from database.db import get_user_emotion_history

songs = pd.read_csv("data/cleaned_spotify.csv")


emotion_genre_map = {

    "joy": ["pop", "dance", "edm"],
    "sadness": ["acoustic", "piano", "indie"],
    "anger": ["rock", "metal"],
    "fear": ["ambient", "lofi"],
    "love": ["romance", "rnb"],
    "surprise": ["electronic", "hiphop"],
    "neutral": songs["track_genre"].unique().tolist()
}


emotion_recovery_map = {

    "sadness": ["sadness", "fear", "joy"],
    "anger": ["anger", "fear", "joy"],
    "fear": ["fear", "joy"],
    "neutral": ["neutral", "joy"],
    "joy": ["joy"]
}


def adjust_with_memory(emotion, playlist):

    history = get_user_emotion_history()

    liked_songs = []

    for past_emotion, song, feedback in history:

        if past_emotion == emotion and feedback == "yes":
            liked_songs.append(song)

    if liked_songs:

        playlist = sorted(
            playlist,
            key=lambda x: x["song"] in liked_songs,
            reverse=True
        )

    return playlist


def recommend_song(emotion):

    playlist = []

    recovery_path = emotion_recovery_map.get(emotion, ["neutral"])

    for stage in recovery_path:

        genres = emotion_genre_map.get(stage, songs["track_genre"].unique())

        filtered = songs[songs["track_genre"].isin(genres)]

        if not filtered.empty:

            sampled = filtered.sample(min(2, len(filtered)))

            for _, row in sampled.iterrows():

                playlist.append({

                    "song": row.get("track_name"),
                    "artist": row.get("artists"),
                    "genre": row.get("track_genre")

                })

    random.shuffle(playlist)

    playlist = playlist[:5]

    playlist = adjust_with_memory(emotion, playlist)

    return playlist

