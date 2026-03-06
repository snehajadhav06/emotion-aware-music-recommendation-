from transformers import pipeline

# Load emotion classification model
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

def detect_emotion(text):
    
    result = emotion_classifier(text)
    
    emotion = result[0][0]["label"]
    score = result[0][0]["score"]
    
    return emotion, score
# Example usage
if __name__ == "__main__":
    
    text = "I feel really frustrated today"
    
    emotion, score = detect_emotion(text)
    
    print("Emotion:", emotion)
    print("Confidence:", score)