#Read index.html file
with open('index.html', 'r') as myfile:
    data=myfile.read()

# Read all the archor element hrefs and set them as name attribute to anchor tag
from bs4 import BeautifulSoup
soup = BeautifulSoup(data)
# Fill all the anchor elements in html file
for anchor in soup.find_all('a'):
    href=anchor["href"]
    # if it is not index.html anchor element, add name attribute
    if "index" not in href:
        anchor["name"]=href.split(".")[0]
        
# Update the index.html file
with open('index.html', 'w') as the_file:
    the_file.write(str(soup))
