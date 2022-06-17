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
    data = f.text
    data = data.replace('\n','')
    a = data.index('document.write(YYsT111);')
    b = data.index('document.write(f00yBelow01);')
    print(data[a:b])
    print()

for i in range(1,10):
    print(f'i = {i}')
    download(f'https://mojim.com/twy100111x105x{i}.htm')
