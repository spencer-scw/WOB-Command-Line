import requests
import sys
from bs4 import BeautifulSoup

def pretty_printing(r) -> str:
    out = ''
    text_lines = [line for line in r.json()["lines"]]
    for line in text_lines:
        soup = BeautifulSoup(line["text"], 'html.parser')
        out = ''.join([out, (f'{line["speaker"]}: {soup.get_text()}'), '\n'])
    return out        

def clean_json(r):
    json = r.json()
    text_lines = [line for line in json["lines"]]
    for line in text_lines:
        soup = BeautifulSoup(line["text"], 'html.parser')
        line["text"] = soup.get_text()
    json["lines"] = text_lines
    return(json)

amount = 1
if any([item in sys.argv for item in ["-a", "--amount"]]):
    if "--amount" in sys.argv: 
        amount = sys.argv[sys.argv.index("--amount") + 1]
    else:
        amount = sys.argv[sys.argv.index("-a") + 1]

for i in range(int(amount)):

    if any([item in sys.argv for item in ["-h", "--help"]]):
        print("""
USAGE: wob [OPTIONS] [AMOUNT]

By default, will print a formatted version of a random Word of Brandon. The following options are also available:

-a | --amount [NUMBER]
    Prints the specified amount of WOBS. By default selects randomly and uses pretty printing.

-c | --clean-json
    Prints the output in json that has had the text cleaned. Similar to -j but without HTML tags
            
-j | --json
    Prints the output in the raw json from the API. Note that the text will contain HTML tags.
            
-s | --search [QUERY]
    Prints the top 5 results by default; specify -a to get more or less. Default is pretty printing.
            """)
    
    elif any([item in sys.argv for item in ["-c", "--clean-json"]]):
        r = requests.get('https://wob.coppermind.net/api/random_entry/?format=json')
        print(clean_json(r))
    
    elif any([item in sys.argv for item in ["-j", "-json"]]):
        r = requests.get('https://wob.coppermind.net/api/random_entry/?format=json')
        print(r.json())
    
    else:
        r = requests.get('https://wob.coppermind.net/api/random_entry/?format=json')
        print(pretty_printing(r))
    
    print()
