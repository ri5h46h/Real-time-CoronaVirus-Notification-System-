from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/uday_/Downloads/coronavirus_Oth_3.ico",
        timeout = 5 
    )

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    
    myHtmlData = getData('https://www.mohfw.gov.in/')
    
    print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    #print(soup.preetify())
    myDatastr = ""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        myDatastr += tr.get_text()
    myDatastr = myDatastr[1:]
    itemList = (myDatastr.split("\n\n"))

    states = ['Gujarat','Bihar']
    for item in itemList[0:32]:
        dataList = item.split('\n')
        if dataList[1] in states:
            print(dataList)
            notiTitle = 'Cases of Covid -19'
            notiText = f"{dataList[1]}\nTotal Cases : {dataList[2]}\nCured : {dataList[3]}\nDeath : {dataList[4]}"
            notifyMe(notiTitle,notiText)
            time.sleep(4)

    