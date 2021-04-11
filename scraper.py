import re
import requests
from bs4 import BeautifulSoup

#response = requests.get('https://www.hangmanwords.com/words')
#print(response.status_code)

def getwords()
response = requests.get('https://www.hangmanwords.com/words')
response = response.content
