import requests
import re
from bs4 import BeautifulSoup

quotes = []
authors = []

page = requests.get("https://www.brainyquote.com/topics/motivational-quotes")
contents = page.content

data = BeautifulSoup(contents, 'html.parser')
unparsed_quotes = data.find_all("a", {"class": "b-qt"})
unparsed_authors = data.find_all("a", {"class": "bq-aut"})
for chunk in unparsed_quotes:
    stringed_chunk = str(chunk)
    html = BeautifulSoup(stringed_chunk, "html.parser")
    quote = html.get_text()
    quotes.append(quote)

for chunk in unparsed_authors:
    stringed_chunk = str(chunk)
    html = BeautifulSoup(stringed_chunk, "html.parser")
    author = html.get_text()
    authors.append(author)
for i in range(0,len(quotes)):
    print("\"" + quotes[i] + "\" -" + authors[i])
#print(len(unparsed_quotess))
#print(len(unparsed_authors))

