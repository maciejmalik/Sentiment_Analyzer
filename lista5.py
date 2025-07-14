import matplotlib.pyplot as plt
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()
df = pd.read_csv("opinie.csv", nrows=50)
compounds = []
data = df["content"]
for _, row in data.items():
    scores = sia.polarity_scores(row)
    print(row)
    print(scores)
    compounds.append(scores["compound"])
bins = [-1, -0.5, -0.1, 0.1, 0.5, 1]
labels = ["Bardzo negatywna", "Negatywna", "Neutralna", "Pozytywna", "Bardzo pozytywna"]

categories = pd.cut(compounds, bins=bins, labels=labels, include_lowest=True)

counts = categories.value_counts()

plt.bar(counts.index, counts.values, color='skyblue', edgecolor='black')

plt.title("Opinie o coca-coli")
plt.xlabel("Opinia")
plt.ylabel("Liczba opini")

plt.show()

