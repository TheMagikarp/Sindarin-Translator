import requests
import html5lib
import pickle
from bs4 import BeautifulSoup

url = "http://www.jrrvf.com/hisweloke/sindar/online/sindar/dict-en-sd.html"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html5lib")
words = soup.find_all("p", class_="sindict")

dictionary = {}

count = 0
for item in words:        
        englishWord = item.find("span", class_="entry").text
        elvishWord = item.find("span", class_="form").text
        POS = item.find_all("i")
        speech = POS[1].text
        dictionary[englishWord] = {}
        dictionary[englishWord][speech] = [elvishWord]

#for i in sorted(dictionary):
        #print(i, dictionary[i])

#with open('sindarin.pickle', 'wb') as handle:
        #pickle.dump(dictionary, handle)
