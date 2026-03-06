import sqlite3
import pandas as pd

conn = sqlite3.connect("musicbot.db")

df = pd.read_sql("SELECT * FROM user_history", conn)

print("\nUser Listening Analytics\n")

print("Most common emotions:")
print(df["emotion"].value_counts())

print("\nFeedback distribution:")
print(df["feedback"].value_counts())

print("\nTop recommended songs:")
print(df["song"].value_counts().head(5))