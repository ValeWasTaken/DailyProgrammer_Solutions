import urllib
from bs4 import BeautifulSoup

def clean(comments):
        clean = []
        for char in comments:
                if str.isalpha(char) == True:
                        clean.append(char)
                elif str.isalpha(char) == False:
                        0
        return clean

def findSentiment(url):
        soup = BeautifulSoup(urllib.urlopen(url).read())
        happy = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
        sad = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst']
        positive, negative = 0,0        
        data = soup.find_all("div", class_="comment-text-content") 
        
        comments = clean((str(data).split()))
        for comment in range(len(comments)):
                if comments[comment].lower() in happy:
                        positive += 1
                if comments[comment].lower() in sad:
                        negative += 1
        print("Happy words: "+str(positive))
        print("Sad words: "+str(negative))
findSentiment(raw_input()) # Example URL: https://www.youtube.com/all_comments?v=2azIwEMJfqY
