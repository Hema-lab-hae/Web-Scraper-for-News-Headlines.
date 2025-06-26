# 📰 Headline Scraper

A simple Python script that scrapes top headlines from a news website (e.g., CNN) using `requests` and `BeautifulSoup`, and saves them to a `.txt` file.

## 🚀 Features
- Scrapes `<h2>` tags from a news site (like CNN)
- Extracts and cleans headline text
- Saves all headlines to a plain text file: `headlines.txt`

## 🛠 Requirements
Make sure Python is installed (Python 3.x recommended). Then install the following packages:

```bash
pip install requests beautifulsoup4

Project Structure
bash
Copy
Edit
web-scraper/
├── scrape_headlines.py     # Main script
├── headlines.txt           # Output file with headlines
└── README.md               # This file

 How It Works
Sends an HTTP GET request to a news website (e.g. CNN).
Parses the HTML response with BeautifulSoup.
Extracts all <h2> elements (usually contain headlines).
Writes each headline to a new line in headlines.txt.

Example Output
headlines.txt:

csharp
Copy
Edit
Supreme Court issues major ruling on guns
Biden announces new student loan forgiveness
Stocks rally after Fed comments
...


