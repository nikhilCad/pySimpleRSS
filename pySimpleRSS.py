import PySimpleGUI as sg
import feedparser
from newspaper import Article

feedlist = [
##    "https://www.thenewsminute.com/kerala.xml",
##    "https://www.thenewsminute.com/tamil.xml",
##    "https://www.thehindu.com/news/national/kerala/feeder/default.rss",
##    "https://www.thehindu.com/news/national/tamil-nadu/feeder/default.rss"
    "http://rss.cnn.com/rss/edition.rss"
    ]

titles = []
links = []

labelList = []


def linkPress(link,title):#keep button functions above button call
    curArticle = Article (link, language="en")
    curArticle.download()
    curArticle.parse()
    #pageLabel.config(text = title + "\n\n" +
    #                 curArticle.text
     #                + curArticle.summary)#Change this later to parsed text

for i in range(len(feedlist)):
    
    tempfeed = feedparser.parse(feedlist[i])

    for j in range(len(tempfeed.entries)):

        titles.append( tempfeed.entries[j].title )
        links.append( tempfeed.entries[j].link ) 


layout = [
    [sg.Column([[sg.Text(f"{titles[i]}", font=("Courier New", -20))] for i in range(len(titles))],
                scrollable=True)]
]



window = sg.Window("pySimpleRSS", layout, margins=(0, 0))

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
window.Close()