import requests
from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    text = ""
    def handle_data(self, data):
        self.text += data

def download(url):
    r = requests.get(url)
    f = HTMLFilter()
    f.feed(r.text)
    print(f.text.replace('\n',''))
    print()

download('https://mojim.com/twy100111x105x1.htm')
download('https://mojim.com/twy100111x105x2.htm')
download('https://mojim.com/twy100111x105x3.htm')