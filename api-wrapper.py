import requests
from bs4 import BeautifulSoup
r = requests.get('https://wob.coppermind.net/api/random_entry/?format=json')
text_lines = [line for line in r.json()["lines"]]

for line in text_lines:
    soup = BeautifulSoup(line["text"], 'html.parser')
    print(f'{line["speaker"]}: {soup.get_text()}')
    print()

