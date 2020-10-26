#TODO: Repeat for remaining pages and consider doing the same for the inspirational quotes as well

import requests
from bs4 import BeautifulSoup
import time
import csv

start_time = time.time()

quotes = []
authors = []
quotes_and_authors = []
base_path = "https://www.brainyquote.com/topics/motivational-quotes"
base_path2 = "https://www.brainyquote.com/topics/inspirational-quotes"
base_path3 = "https://www.brainyquote.com/topics/wisdom-quotes"

for i in range(1,68):
    if i is not 1 and i <= 11:
        page = requests.get(base_path + "_" + str(i))
    elif i is 12:
        page = requests.get(base_path2)
    elif i >= 13 and i <= 29:
        page = requests.get(base_path2 + "_" + str(i - 11))
    elif i is 30:
        page = requests.get(base_path3)
    elif i >= 31:
        page = requests.get(base_path3 + "_" + str(i-30))
    else:
        page = requests.get(base_path)

    contents = page.content

    data = BeautifulSoup(contents, 'html.parser')
    unparsed_quotes = data.find_all("a", {"class": "b-qt"})
    unparsed_authors = data.find_all("a", {"class": "bq-aut"})
    for chunk in unparsed_quotes:
        stringed_chunk = str(chunk)
        html = BeautifulSoup(stringed_chunk, "html.parser")
        quote = html.get_text()
        quotes.append(quote)
        #print(quote)

    for chunk in unparsed_authors:
        stringed_chunk = str(chunk)
        html = BeautifulSoup(stringed_chunk, "html.parser")
        author = html.get_text()
        authors.append(author)

end_time = time.time()
time_used = int(end_time - start_time)

for i in range(0,len(quotes)):
    print(quotes[i] + " - " + authors[i])
    quotes_and_authors.append((quotes[i], authors[i]))
    #print(len(unparsed_quotess))
    #print(len(unparsed_authors))

quotes_and_authors = list(set(quotes_and_authors))

with open("quotes.csv", "w") as output_file:
    writer = csv.writer(output_file)
    for line in quotes_and_authors:
        writer.writerow([line[0], line[1]])


print("\n\nScraped a total of " + str(len(quotes_and_authors)) + " quotes in " + str(time_used)
      + "\nseconds.......because i'm a fuckin' boss")




