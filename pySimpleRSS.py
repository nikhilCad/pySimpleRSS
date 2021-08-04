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
    [sg.Column([[sg.Button(button_text = f"{titles[i]}", font=("Courier New", -20))] for i in range(len(titles))],
                scrollable=True, vertical_scroll_only=True )]
]


window = sg.Window("pySimpleRSS", layout, margins=(0, 0), resizable=True)

def openWindow(title):
    layout2 = [
        [sg.Column([[sg.Button(button_text = "Hello", font=("Courier New", -20))] ],
                scrollable=True, vertical_scroll_only=True )]
        ]
    window2 = sg.Window("pySimpleRSS", layout2, margins=(0, 0), resizable=True)

    while True:
        event, values = window2.Read()
        if event is None or event == 'Exit':
            break
        window2.Close()

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event in titles:
        openWindow(event)

window.Close()