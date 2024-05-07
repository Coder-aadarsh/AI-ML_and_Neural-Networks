import tkinter as tk
import nltk
# Natural Language Processing Toolkit
from textblob import TextBlob
# Sentiment Analysis Tool
from newspaper import Article


def summarize():
    # Get URL from user input
    url = utext.get('1.0', "end").strip()

    # Download and parse the article
    ar = Article(url)
    ar.download()
    ar.parse()
    ar.nlp()

    # Enable text fields for displaying results
    title.config(state='normal')
    author.config(state='normal')
    publish.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clear previous content in text fields
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publish.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')

    # Display article details
    title.insert('1.0', ar.title)
    author.insert('1.0', ar.authors)
    publish.insert('1.0', ar.publish_date)
    summary.insert('1.0', ar.summary)

    # Perform Sentiment Analysis
    analysis = TextBlob(ar.text)
    # Display sentiment analysis result
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Disable text fields after displaying results
    title.config(state='disabled')
    author.config(state='disabled')
    publish.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


def clear_fields():
    # Clear all text fields
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publish.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')
    utext.delete('1.0', 'end')


# Now we will Build GUI using TK
root = tk.Tk()
root.title("Post Summarizer")
root.geometry('1200x650')

# Labels for each text field
tlable = tk.Label(root, text="TITLE")
tlable.pack()

alable = tk.Label(root, text="AUTHOR")
alable.pack()

plable = tk.Label(root, text="PUBLISHING DATE")
plable.pack()

slable = tk.Label(root, text="SUMMARY")
slable.pack()

selable = tk.Label(root, text="SENTIMENT")
selable.pack()

ulable = tk.Label(root, text="ENTER URL HERE")
ulable.pack()

# Text fields for displaying results
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='black', foreground="white")
title.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='black', foreground="white")
author.pack()

publish = tk.Text(root, height=1, width=140)
publish.config(state='disable', bg='black', foreground="white")
publish.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='black', foreground="white")
summary.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='black', foreground="white")
sentiment.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

# Buttons for Summarize and Clear
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

btn_clear = tk.Button(text="Clear", command=clear_fields, font=('Helvetica', 14, 'bold'))
btn_clear.pack()

root.mainloop()
