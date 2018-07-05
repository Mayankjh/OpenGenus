from bs4 import BeautifulSoup
from collections import Counter
import requests
from urllib.request import urlopen

# takes url
urUrl = input("Enter Your Url:-")
#opens Url
html = urlopen(urUrl)
#reads page
a= len(html.read())/1024
print('The size of url in kbs is:-',a)
soup = BeautifulSoup(requests.get(urUrl).text, "html.parser")

foundUrls = Counter([link["href"] for link in soup.find_all("a", href=lambda href: href and not href.startswith("#"))])
foundUrls = foundUrls.most_common()

count = 0
for item in foundUrls:
    print ("%s: %d" % (item[0], item[1]))
    count = count +1

print('The no. <a> tags are:- ',count)
