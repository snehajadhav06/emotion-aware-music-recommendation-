from models.emotion_detector import detect_emotion
from recommender.song_recommender import recommend_song


def emotion_chat_with_music(user_message):
    """
    Detect emotion from the user's message,
    respond empathetically, and generate a playlist.
    """

    # Detect emotion using the ML model
    emotion, score = detect_emotion(user_message)

    # Supportive chatbot responses
    responses = {
        "sadness": "I'm really sorry you're feeling sad. Music can sometimes help lift your mood.",
        "anger": "It sounds like you're feeling frustrated. Let's try something calming.",
        "fear": "That sounds stressful. Maybe relaxing music can help.",
        "joy": "That's great to hear! Let's keep the good vibes going with some music.",
        "love": "That's a beautiful feeling. Here's something romantic.",
        "surprise": "Sounds exciting! Let's add some energetic music.",
        "neutral": "Thanks for sharing. Here's something nice to listen to."
    }

    # Select appropriate response
    response = responses.get(
        emotion,
        "Thanks for sharing how you feel. Here is some music you might enjoy."
    )

    # Generate playlist
    playlist = recommend_song(emotion)

    # Return structured response
    return {
        "emotion": emotion,
        "confidence": score,
        "response": response,
        "playlist": playlist
    }

