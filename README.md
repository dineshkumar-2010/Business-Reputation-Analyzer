# Business Reputation & Insights Analyzer using Google Maps Reviews + LLMs

An AI-powered analytics dashboard that processes Google Maps reviews to extract business insights using sentiment analysis, topic extraction, trend analysis, and recommendation generation.

## Project Overview

Local businesses receive thousands of customer reviews on Google Maps. These reviews are unstructured and difficult to analyze manually.

This project helps businesses analyze customer feedback automatically by extracting sentiment, recurring themes, trends, and improvement recommendations.

---

## Features

- Sentiment Classification (Positive / Neutral / Negative)
- Topic Extraction (Food Quality, Pricing, Delivery, Staff, Cleanliness, Ambience)
- Review Trend Analysis Over Time
- AI-generated Business Improvement Recommendations
- Customer Feedback Summary
- Interactive Streamlit Dashboard
- Business-wise comparison

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Matplotlib
- Hugging Face Transformers
- SerpAPI
- Google Maps Reviews API
- Hugging Face Spaces

---

## Project Workflow

### 1. Data Collection
Collected customer reviews using Google Maps Reviews / SerpAPI.

### 2. Data Preprocessing
- Remove duplicates
- Remove missing values
- Clean text
- Tokenization
- Stopword filtering

### 3. Model Development
- Sentiment Classification
- Topic Extraction
- Review analysis

### 4. Recommendation Generation
- Operational improvement suggestions
- Trend-based recommendations
- Competitor insights

### 5. Deployment
Built and deployed using Streamlit.

---

## Dashboard Features

- Business Filter
- Sentiment Distribution Chart
- Rating Trend Over Time
- Top 5 Positive Themes
- Top 5 Negative Themes
- Auto-generated Recommendations
- AI Summary
- Dataset Preview

---

## Folder Structure

Business-Reputation-Analyzer/

│── app.py

│── README.md

│── requirements.txt

│── final_reviews_analysis.json

│── cleaned_reviews.json

│── business.ipynb
