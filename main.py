import requests
from bs4 import BeautifulSoup

# Step 1: Set the target news website
url = 'https://www.cnn.com'  # You can change this to any news site

# Step 2: Send a GET request to fetch the HTML content
response = requests.get(url)

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Step 4: Find all <h2> tags (commonly used for headlines)
headlines = soup.find_all('h2')

# Step 5: Extract text content from each headline
headline_texts = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

# Step 6: Save the headlines to a .txt file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for line in headline_texts:
        file.write(line + '\n')

print(f"✅ {len(headline_texts)} headlines saved to 'headlines.txt'")
