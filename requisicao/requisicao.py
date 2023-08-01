import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3000/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
print(parsed_html.handle_endtag)



