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

def updateFeed():
    for i in range(len(feedlist)):
        
        tempfeed = feedparser.parse(feedlist[i])

        for j in range(len(tempfeed.entries)):

            if tempfeed.entries[j].title not in titles:

                titles.append( tempfeed.entries[j].title )
                links.append( tempfeed.entries[j].link ) 

updateFeed()

sg.theme('DarkAmber')

layout1 = [

    [sg.Button("ADD FEED", size=(15, 1)), sg.InputText()],

    [sg.Column([[sg.Button(button_text = f"{titles[i]}", font=("Courier New", -20))] for i in range(len(titles))],
                scrollable=True, vertical_scroll_only=True )]
]

charsEach = 120 #chars in each line in article full text view

boxText = "lolxd"

layout2 = [


         [sg.Column([  [sg.Text(text = boxText , font=("Courier New", -20),
          size =( charsEach, None ))]   ],
                 scrollable=True, vertical_scroll_only=True, key="fullText" )],
                 [sg.Button('Back')]
        #Column is used JUST to get the scrollbar and nothing else

         #[sg.Text(boxText, size =(charsEach, None))]
         #This works but no scrollbar

        ]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-')]]


window = sg.Window("pySimpleRSS", layout, margins=(0, 0), resizable=True)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

    if event in titles:
        window["-COL1-"].update(visible=False)

        link = ""

        for i in range(len(titles)):
            if titles[i] == event:
                link = links[i]
        

        boxText = linkPress(link)

        print(boxText)

        #THIS LINE IS BUGGYYYYYYYYYYYYYYYYYYY
        window["fullText"] = boxText

        window["-COL2-"].update(visible=True)
        
    
    if event == "Back":
        window["-COL2-"].update(visible=False)
        window["-COL1-"].update(visible=True)
    
    if values[0] != None:#Add feed button
        print(values[0])

window.Close()