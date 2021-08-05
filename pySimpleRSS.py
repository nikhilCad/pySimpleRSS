import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Multiline
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


def linkPress(link):#keep button functions above button call
    curArticle = Article (link, language="en")
    curArticle.download()
    curArticle.parse()
    return curArticle.text
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

    link = ""

    for i in range(len(titles)):
        if titles[i] == title:
            link = links[i]
    
    print(link)

    boxText = linkPress(link)

    print(boxText)

    charsEach = 120 #chars in each line

    layout2 = [


         [sg.Column([[sg.Text(text = boxText , font=("Courier New", -20),
          size =( charsEach, None ))] ],
                 scrollable=True, vertical_scroll_only=True )]
        #Column is used JUST to get the scrollbar and nothing else

         #[sg.Text(boxText, size =(charsEach, None))]
         #This works but no scrollbar

        ]
        #size has width in chars first, height in rows later
    window2 = sg.Window(title, layout2, margins=(0, 0), resizable=True)

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