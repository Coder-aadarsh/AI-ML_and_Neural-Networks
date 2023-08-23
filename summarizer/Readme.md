# Post Summarizer

A Python program that extracts and summarizes information from online articles, along with sentiment analysis, using natural language processing libraries.

## Intro

This program uses the `tkinter` library to create a graphical user interface (GUI) for summarizing articles from URLs. It fetches the article content using the `newspaper` library, performs natural language processing with `TextBlob` for sentiment analysis, and displays the extracted information in the GUI.
## Features

- Extracts and displays the title, author, publishing date, summary, and sentiment analysis of an article from a given URL.
- User-friendly GUI interface for inputting URLs and viewing summarized results.
- Sentiment analysis indicates whether the sentiment is positive, negative, or neutral.

## Deployment Instructions

1. Clone the repository:
```bash
git clone https://github.com/aadarsh-nagrath/summarizer.git
```
2. Navigate to the repository directory:
```bash
cd summarizer
```
3. Install the required dependencies. Make sure you have newspaper3k and textblob libraries installed:
```bash   
pip install newspaper3k textblob
```
4. Run the program:
```bash
python main.py
```
5. The GUI window will appear. Enter the URL of the article you want to summarize and click the "Summarize" button.

6. The article's information, including sentiment analysis, will be displayed in the text fields.

7. To clear all fields, click the "Clear" button.

## Dependencies

-  tkinter: Python's standard GUI library.
-  newspaper3k: For extracting article content from URLs.
-  textblob: For performing sentiment analysis on the article's text.

    ```bash
    pip install textblob newspaper
    ```
    
## Author
Aadarsh Nagrath
