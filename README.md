# Coca-Cola Review Sentiment Analysis

This project scrapes user reviews of Coca-Cola from Trustpilot and analyzes their sentiment using the NLTK library in Python.

## 📄 Overview

The project consists of two main parts:
1. **Web Scraper (`scrapper.py`)** – Collects user reviews rustpilot and saves them to a CSV file (`opinie.csv`).
2. **Sentiment Analysis (`Sentiment.py`)** – Uses NLTK's `SentimentIntensityAnalyzer` to assess the sentiment of each review and visualizes the results as a bar chart.

## 📊 Sample Output
The output chart categorizes reviews as:
- Bardzo negatywna *(Very negative)*
- Negatywna *(Negative)*
- Neutralna *(Neutral)*
- Pozytywna *(Positive)*
- Bardzo pozytywna *(Very positive)*
- 
## 🛠️ Technologies
- Python
- NLTK (SentimentIntensityAnalyzer)
- BeautifulSoup (Web scraping)
- Matplotlib
- Pandas


This project is for educational purposes only. The data was collected from publicly available reviews on [Trustpilot](https://www.trustpilot.com).
