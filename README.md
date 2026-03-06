# 🎧 Emotion-Aware Music Chatbot

An AI-powered chatbot that detects a user's emotional state from text and recommends music accordingly.
The system analyzes user input, identifies emotions using a transformer-based NLP model, and suggests songs that help improve or match the user's mood.

---

## 🚀 Features

* Detects user emotions from text
* Recommends songs based on emotional state
* Interactive chatbot interface
* Mood transition logic to gradually improve user's mood
* Simple dashboard for analytics

---

## 🧠 Tech Stack

* **Python**
* **Transformers (HuggingFace)**
* **PyTorch**
* **Streamlit**
* **Pandas / NumPy**
* **Spotify Features API (optional)**

---

## 📂 Project Structure

```
emotion-music-ai
│
├── data
│   └── songs_dataset.csv
│
├── models
│   └── emotion_detector.py
│
├── recommender
│   └── song_recommender.py
│
├── chatbot
│   └── chat_logic.py
│
├── database
│   └── db.py
│
├── dashboard
│   └── analytics.py
│
├── ui
│   └── app.py
│
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/emotion-music-chatbot.git
```

Move into the project folder:

```
cd emotion-music-chatbot
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run ui/app.py
```

The app will open in your browser.

---

## 💡 Example

User Input:

```
I feel very lonely today
```

Detected Emotion:

```
Sadness
```

Recommended Music:

```
Calming / uplifting songs
```

---

## 📊 Future Improvements

* Voice emotion detection
* Real-time Spotify integration
* Personalized music recommendations
* User mood tracking dashboard

---

## 👩‍💻 Author

Sneha Jadhav
Engineering Student | Aspiring ML Engineer

---

## ⭐ If you like this project

Give the repository a **star** ⭐
