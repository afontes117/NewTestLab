# Importing modules since they aren't built-in to the Python language 
from urllib.request import urlopen
from bs4 import BeautifulSoup 

# Making a request to get a webpage
url = 'https://spacejam.com/' 
html_doc = urlopen(url)

# Beautiful Soup parsing the page 
soup = BeautifulSoup(html_doc, 'html.parser')

# Get and output title of web page 
title = soup.title.string 
print("title of page: ", title)

# Get all links on page 
links_list = soup.find_all('a')

# Loop through all link tags and print just link (instead of <a href=""...>") 
# Block has been commented out 
'''
for link in links_list:
    print(link.get('href'))
'''

# Get all text on page 
text = soup.get_text()

# Find all font tags 
fonts = soup.find_all('font')

# Find all tags with class of footer-links 
footers = soup.find_all(class_="footer-links")

# List to store all footer links 
footer_link_list = [] 

# Dictionary (Hashmap) to store only unique top level domains 
tld_count = {} 

# For every footer on page, parse to get only link
# If it links somewhere else (has '.' in the url),
# Increment its entry in the tld_count dictionary 

for footer in footers:
    # print(footer.a)
    link = footer.a.get('href')
    print(link)
    footer_link_list.append(link)
    
    if '.' in link: 
        seperated_link_as_list = link.split('.') 
        tld = seperated_link_as_list[-2] 
        
        if tld not in tld_count: 
            tld_count[tld] = 1 
        else:
            tld_count[tld] += 1 
            


