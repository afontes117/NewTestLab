# Importing modules since they aren't built-in to the Python language 
from urllib.request import urlopen
from bs4 import BeautifulSoup 

# Making a request to get a webpage
url = 'https://evanyou.me/' 
html_doc = urlopen(url)

# Beautiful Soup parsing the page 
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

print (soup.p.string)
soup.find_all('p')
plist= soup.find_all('p')



for p in plist:
    print(p.text)
