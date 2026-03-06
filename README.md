# 🎧 Emotion-Aware Music Recommendation Chatbot

An AI-powered music assistant that detects a user's emotional state and recommends songs that match or improve their mood.

The system uses **Natural Language Processing and Transformer models** to analyze user input, identify emotions, and generate personalized music recommendations. The application also stores user interactions and visualizes mood patterns over time.

---

## 🌐 Live Demo

Try the application here:

**🔗 https://emotion-music-recommendation-chat.streamlit.app**

---

## 🚀 Features

* 🧠 Emotion detection using transformer-based NLP models
* 🎵 AI-powered music recommendations based on mood
* 💬 Interactive wellness chatbot interface
* 🎤 Voice input support
* 📊 Mood analytics dashboard with trend visualization
* 💾 Feedback system for improving recommendations

---

## 🧠 Tech Stack

**Programming & Frameworks**

* Python
* Streamlit

**Machine Learning**

* HuggingFace Transformers
* PyTorch

**Data Processing**

* Pandas
* NumPy

**Visualization**

* Plotly

**Database**

* SQLite

---

## 📂 Project Structure

```
emotion-music-chatbot
│
├── chatbot
│   └── chat_logic.py
│
├── database
│   └── db.py
│
├── models
│   └── emotion_detector.py
│
├── recommender
│   └── song_recommender.py
│
├── utils
│   ├── album_art.py
│   └── voice_input.py
│
├── ui
│   └── app.py
│
├── data
│   └── songs_dataset.csv
│
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/snehajadhav06/emotion-aware-music-recommendation.git
```

Navigate into the project directory

```
cd emotion-aware-music-recommendation
```

Create a virtual environment

```
python -m venv venv
```

Activate the environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app

```
streamlit run ui/app.py
```

The application will open in your browser.

---

## 💡 Example Interaction

**User Input**

```
I feel very lonely today
```

**Detected Emotion**

```
Sadness
```

**Recommended Songs**

* Calm acoustic music
* Mood-lifting tracks
* Relaxing playlists

---

## 📊 Mood Analytics

The application stores user interactions and visualizes emotional patterns using a dashboard that includes:

* Mood score trends
* Emotion distribution
* User feedback insights

---

## 🔮 Future Improvements

* 🎤 Real-time voice emotion detection
* 🎧 Spotify API integration for direct playback
* 🤖 Personalized recommendation model
* 📈 Advanced mood tracking and insights

---

## 👩‍💻 Author

**Sneha Jadhav**
Engineering Student | Aspiring Machine Learning Engineer

GitHub: https://github.com/snehajadhav06

---

## ⭐ Support

If you found this project interesting, please consider giving it a **star ⭐ on GitHub**.
It helps others discover the project!
