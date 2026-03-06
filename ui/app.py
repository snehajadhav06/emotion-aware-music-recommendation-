import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

from chatbot.chat_logic import emotion_chat_with_music
from database.db import save_feedback, init_db
from utils.voice_input import record_voice
from utils.album_art import get_album_art
# Initialize database (important for Streamlit Cloud)
init_db()

# Page Config
st.set_page_config(page_title="VibeCheck | AI Music", page_icon="🎧", layout="wide")

# -------------------------------
# THEME ENGINE & SIDEBAR
# -------------------------------
themes = {
    "Midnight Blue": {
        "bg": "linear-gradient(-45deg, #020617, #1e1b4b, #312e81, #020617)",
        "accent": "#1DB954",
        "card_bg": "rgba(15, 23, 42, 0.4)"
    },
    "Deep Forest": {
        "bg": "linear-gradient(-45deg, #064e3b, #022c22, #065f46, #022c22)",
        "accent": "#10b981",
        "card_bg": "rgba(2, 44, 34, 0.5)"
    },
    "Sunset Purple": {
        "bg": "linear-gradient(-45deg, #4c1d95, #2e1065, #701a75, #4c1d95)",
        "accent": "#f472b6",
        "card_bg": "rgba(46, 16, 101, 0.4)"
    }
}

with st.sidebar:
    st.title("Settings ⚙️")
    selected_theme = st.selectbox("Choose Visual Experience", list(themes.keys()))
    theme_data = themes[selected_theme]
    
    st.divider()
    st.subheader("Danger Zone")
    
    # Initialize delete confirmation state
    if "confirm_delete" not in st.session_state:
        st.session_state.confirm_delete = False

    if not st.session_state.confirm_delete:
        if st.button("🗑️ Clear History", type="secondary", use_container_width=True):
            st.session_state.confirm_delete = True
            st.rerun()
    else:
        st.warning("Are you sure? This deletes all saved moods.")
        col_yes, col_no = st.columns(2)
        
        # Fixed: Removed 'font_weight' argument
        if col_yes.button("Yes, Delete", type="primary", use_container_width=True):
            conn = sqlite3.connect("musicbot.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM user_history")
            conn.commit()
            conn.close()
            st.session_state.messages = [] # Clear chat too
            st.session_state.confirm_delete = False
            st.success("History wiped!")
            st.rerun()
            
        if col_no.button("Cancel", use_container_width=True):
            st.session_state.confirm_delete = False
            st.rerun()

# -------------------------------
# DYNAMIC UI STYLE
# -------------------------------
st.markdown(f"""
<style>
    @keyframes gradientBG {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    .stApp {{
        background: {theme_data['bg']};
        background-size: 400% 400%;
        animation: gradientBG 20s ease-in-out infinite;
        color: #f8fafc;
    }}

    .stTabs [data-baseweb="tab-list"] {{
        gap: 50px; 
        background-color: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        padding: 20px 40px;
        border-radius: 25px;
        margin-bottom: 3rem;
        justify-content: center;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        height: 60px;
        color: #94a3b8;
        font-weight: 700;
        letter-spacing: 1.2px;
        text-transform: uppercase;
    }}

    .stTabs [aria-selected="true"] {{
        background-color: {theme_data['accent']}22 !important;
        color: {theme_data['accent']} !important;
    }}

    .song-card {{
        background: {theme_data['card_bg']};
        backdrop-filter: blur(15px) saturate(150%);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        margin-bottom: 25px;
    }}
    
    .song-title {{ font-size: 1.5rem; font-weight: 800; color: white; }}
    .song-meta {{ color: {theme_data['accent']}; font-weight: 600; }}

    .play-link {{
        display: inline-flex;
        padding: 12px 28px;
        background: {theme_data['accent']};
        color: white !important;
        border-radius: 50px;
        text-decoration: none !important;
        font-weight: 700;
    }}

    .stButton button {{
        border-radius: 30px !important;
        background-color: {theme_data['accent']} !important;
        color: white !important;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🎧 VibeCheck</h1>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["✨ Recommender", "💬 Support Chat", "📈 Mood Insights"])

# -------------------------------
# TAB 1 : MUSIC RECOMMENDER
# -------------------------------
with tab1:
    user_input = st.text_input("How are you feeling?", placeholder="Describe your mood...", key="recommender_input")
    if st.button("🎤 Record Voice", key="voice_btn"):
        voice_text = record_voice()
        if voice_text:
            st.success(f"Captured: {voice_text}")
            user_input = voice_text

    if user_input:
        result = emotion_chat_with_music(user_input)
        emotion, playlist = result["emotion"], result["playlist"]

        st.markdown(f"### Detected Resonance: <span style='color:{theme_data['accent']}'>{emotion.upper()}</span>", unsafe_allow_html=True)

        for i, song in enumerate(playlist, start=1):
            image = get_album_art(song["song"], song["artist"])
            st.markdown('<div class="song-card">', unsafe_allow_html=True)
            col1, col2 = st.columns([1,3])
            with col1:
                st.image(image if image else "https://via.placeholder.com/300", width=200)
            with col2:
                st.markdown(f'<div class="song-title">{song["song"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="song-meta">{song["artist"]} • {song["genre"]}</div>', unsafe_allow_html=True)
                query = f"{song['song']} {song['artist']}".replace(" ","+")
                st.markdown(f'<a href="https://www.youtube.com/results?search_query={query}" class="play-link">▶ EXPLORE</a>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            feedback = st.radio("Is this a match?", ["yes","no"], horizontal=True, key=f"f_{i}")
            if st.button("Rate", key=f"s_{i}"):
                save_feedback(emotion, song["song"], song["artist"], feedback)
                st.toast("Harmony Saved!")

# -------------------------------
# TAB 2 : CHATBOT
# -------------------------------
with tab2:
    st.header("🧠 Wellness Assistant")
    if "messages" not in st.session_state: st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])

    prompt = st.chat_input("What's on your mind?")
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        result = emotion_chat_with_music(prompt)
        assistant_text = f"{result['response']}\n\nResonance: **{result['emotion']}**"

        with st.chat_message("assistant"):
            st.markdown(assistant_text)
            for song in result["playlist"][:3]:
                q = f"{song['song']} {song['artist']}".replace(" ","+")
                st.markdown(f"🎵 **{song['song']}** — {song['artist']} [[▶]](https://www.youtube.com/results?search_query={q})")
        st.session_state.messages.append({"role": "assistant", "content": assistant_text})

# -------------------------------
# TAB 3 : ANALYTICS
# -------------------------------
with tab3:
    st.header("Mood Analytics 📊")
    conn = sqlite3.connect("musicbot.db")
    df = pd.read_sql("SELECT * FROM user_history", conn)
    conn.close()

    if df.empty:
        st.info("No data points detected yet.")
    else:
        # Fixed timestamp parsing
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors='coerce', format='mixed')
        df = df.dropna(subset=["timestamp"])

        emotion_score = {"joy":90, "sadness":20, "anger":30, "fear":40, "love":95, "surprise":70, "neutral":50}
        df["mood_score"] = df["emotion"].map(emotion_score).fillna(50)

        c1, c2, c3 = st.columns(3)
        c1.metric("Avg Mood", f"{int(df['mood_score'].mean())}/100")
        c2.metric("Insights", len(df))
        c3.metric("Top Vibe", df["emotion"].mode()[0].upper() if not df.empty else "N/A")

        st.divider()
        fig = px.line(df, x="timestamp", y="mood_score", markers=True, template="plotly_dark",
                     hover_data={"song": True, "artist": True, "emotion": True})
        fig.update_traces(line_color=theme_data['accent'])
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Recent Echoes")
        st.dataframe(df.sort_values("timestamp", ascending=False).head(15), use_container_width=True)