import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# App title
st.title("CORD-19 Research Dashboard")

st.title("CORD-19 Research Dashboard")

# Load the dataset automatically (no upload needed)
@st.cache_data  # cache so it doesn’t reload every time
def load_data():
    df = pd.read_csv("df_cleaned.csv")
    # Make sure publish_time is datetime
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["publish_year"] = df["publish_time"].dt.year
    return df

df = load_data()

# Show preview
st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Publications Over Time")
pubs_per_year = df["publish_year"].value_counts().sort_index()
st.line_chart(pubs_per_year)

st.subheader("Top Journals")
top_journals = df["journal"].value_counts().head(10)
st.bar_chart(top_journals)

st.subheader("Word Cloud of Titles")
text = " ".join(df["title"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
