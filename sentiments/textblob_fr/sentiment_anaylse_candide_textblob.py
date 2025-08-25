import requests
import re
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer
import pandas as pd
from plotnine import *

def fetch_text_from_github(github_url):
    response = requests.get(github_url)
    if response.status_code == 200:
        return response.text
    else:
        print("Fehler beim Abrufen des Textes von GitHub.")
        return None

# Lade den französischen Text
github_url = "https://raw.githubusercontent.com/MiMoText/roman18/master/plain/files/Voltaire_Candide.txt"
voltaire_candide = fetch_text_from_github(github_url)

# Kapitel anhand von "CHAPITRE" trennen 
voltaire_candideParts = re.split(r'CHAPITRE', voltaire_candide)

# Erster Split-Teil ist Vorspann → überspringen
allChapters = [ch.strip() for ch in voltaire_candideParts[1:] if ch.strip()]

chapter_sentiments = []
for i, chapter in enumerate(allChapters, 1):
    blob = TextBlob(chapter, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    sentiments = []
    for sent in blob.sentences:
        s = sent.sentiment
        if s is not None and isinstance(s, tuple):
            sentiments.append(s[0])  # Polarität
    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
    chapter_sentiments.append(avg_sentiment)

# DataFrame erstellen
chapters_df = pd.DataFrame({
    'Kapitel': list(range(1, len(chapter_sentiments) + 1)),
    'Polarität': chapter_sentiments
})

# Visualisierung mit ggplot
plot = (
    ggplot(chapters_df, aes(x='Kapitel', y='Polarität')) +
    geom_bar(stat='identity', fill="#69b3a2", color="black", alpha=0.7) +
    #geom_smooth(method='lm', color='red', se=False, size=1.2) +
    labs(
        #title='Sentiment-Analyse mit TextBlob-fr: Candide',
        x='Kapitel',
        y='Durchschnittliche Polarität'
    ) +
    theme_minimal() +
    theme(
        axis_text_x=element_text(rotation=0, size=9),
        axis_text_y=element_text(size=9),
        plot_title=element_text(size=12, weight='bold', ha='center')
    )
)

# Plot anzeigen und speichern
print(plot)
plot.save("candide_sentiment_analysis_fr.png", dpi=300)
print("Plot wurde gespeichert.")
