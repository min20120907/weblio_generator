from bs4 import BeautifulSoup
import requests

# List of query words
query_texts = ["word1", "word2", "word3"]

# Iterate over the query words
for i in range(len(query_texts)):
    url = "https://www.weblio.jp/content/" + query_texts[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the main content div
    content_div = soup.find('div', class_='kijiWrp')

    # Extract the text from the content div
    content_text = content_div.get_text()

    print(content_text)
