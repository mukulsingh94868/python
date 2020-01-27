import urllib.request as url
from bs4 import BeautifulSoup
webpage = "https://www.google.com"
htmlOnPage = url.urlopen(webpage)
soup = BeautifulSoup(htmlOnPage,'html.parser')

#print(soup.prettify())
#print(soup.title)
#print(soup.head.string)
#print(soup.body)
#print(soup.div)
#print(soup.find_all('href'))
#for word in soup.find_all("a"):
	#print(word.get('href'))
#print(soup.getText())	
print(soup.p)