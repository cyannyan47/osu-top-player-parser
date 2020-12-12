from bs4 import BeautifulSoup
html = "<html><body><tr><td><a href='foo'/></td></tr></body></html>"
soup = BeautifulSoup(html, 'lxml')

for ana in soup.findAll('a'):
    print(ana)
    if ana.parent.name == 'td':
        print(ana["href"])