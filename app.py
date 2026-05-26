import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Config (must be first)
# -----------------------------
st.set_page_config(
    page_title="Business Reputation Analyzer",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_json("final_reviews_analysis.json")

df = load_data()

# -----------------------------
# Title
# -----------------------------
st.title("📊 Business Reputation & Insights Analyzer")
st.write("Google Maps Reviews + LLM Analysis Dashboard")

# -----------------------------
# Sidebar Filter
# -----------------------------
businesses = df["Business_Name"].unique()

selected_business = st.sidebar.selectbox(
    "Select Business",
    businesses
)

filtered_df = df[df["Business_Name"] == selected_business]

# -----------------------------
# Overview Metrics
# -----------------------------
st.subheader(f"Overview: {selected_business}")

col1, col2, col3 = st.columns(3)

col1.metric("Total Reviews", len(filtered_df))
col2.metric("Average Rating", round(filtered_df["Rating"].mean(), 2))

positive_count = (
    filtered_df["LLM_Sentiment"]
    .astype(str)
    .str.lower()
    .eq("positive")
    .sum()
)

col3.metric("Positive Reviews", positive_count)

# -----------------------------
# Sentiment Chart
# -----------------------------
st.subheader("📈 Sentiment Distribution")

sentiment_counts = (
    filtered_df["LLM_Sentiment"]
    .astype(str)
    .str.lower()
    .value_counts()
)

fig, ax = plt.subplots()
sentiment_counts.plot(kind="bar", ax=ax)
ax.set_title("Sentiment Count")
ax.set_xlabel("Sentiment")
ax.set_ylabel("Reviews")

st.pyplot(fig)

# -----------------------------
# Top Positive Themes
# -----------------------------
st.subheader("✅ Top 5 Positive Themes")

positive_reviews = filtered_df[
    filtered_df["LLM_Sentiment"]
    .astype(str)
    .str.lower() == "positive"
]

positive_topics = (
    positive_reviews["Topic"]
    .value_counts()
    .head(5)
)

st.dataframe(positive_topics)

# -----------------------------
# Top Negative Themes
# -----------------------------
st.subheader("❌ Top 5 Negative Themes")

negative_reviews = filtered_df[
    filtered_df["LLM_Sentiment"]
    .astype(str)
    .str.lower() == "negative"
]

negative_topics = (
    negative_reviews["Topic"]
    .value_counts()
    .head(5)
)

st.dataframe(negative_topics)

# -----------------------------
# Auto Business Tips
# -----------------------------
st.subheader("💡 Auto-Generated Business Improvement Tips")

if len(negative_topics) == 0:
    st.success("No major negative trends found.")
else:
    for topic, count in negative_topics.items():

        if topic == "Service/Staff":
            st.warning(
                f"{count} complaints on staff/service → Improve customer handling & training."
            )

        elif topic == "Pricing":
            st.warning(
                f"{count} complaints on pricing → Review pricing or combo offers."
            )

        elif topic == "Delivery/Waiting":
            st.warning(
                f"{count} complaints on waiting → Reduce queue and improve delivery speed."
            )

        elif topic == "Food Quality":
            st.warning(
                f"{count} complaints on food quality → Improve consistency and freshness."
            )

        elif topic == "Cleanliness":
            st.warning(
                f"{count} complaints on cleanliness → Strengthen hygiene checks."
            )

        elif topic == "Ambience":
            st.warning(
                f"{count} complaints on ambience → Improve comfort and seating."
            )

        else:
            st.warning(
                f"{count} complaints in {topic} → Investigate recurring issues."
            )

# -----------------------------
# Raw Data
# -----------------------------
st.subheader("📋 Dataset Preview")
st.dataframe(filtered_df.head(20))