#This code is contributed by Rishabh Narayan 
from bs4 import BeautifulSoup #pip install bs4
import requests #pip install requests
from plyer import notification #pip install plyer

# Defining the necessary functions
def getData(url):
    r = requests.get(url)
    return r.text

def notify_me(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = None,
        timeout = 10,
    )

#the main program starts from here...
if __name__ == "__main__":

    myHtmlData = getData('https://www.mohfw.gov.in/')
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    # print(soup.prettify())

    active_cases = soup.find("li", {'class': 'bg-blue'}).find('strong').get_text()
    Cured_Discharged = soup.find("li", {'class': 'bg-green'}).find('strong').get_text()
    Deaths = soup.find("li", {'class': 'bg-red'}).find('strong').get_text()
    Total_cases = int(active_cases) + int(Cured_Discharged) + int(Deaths)
    # print(Total_cases)

    notify_title = "COVID-19 Status (Source : https://www.MoHFW.gov.in/)"
    notify_text = f"Confirmed : {Total_cases}\nActive Cases : {active_cases}\nCured/Discharged : {Cured_Discharged}\nDeaths : {Deaths}" # Used a f string here
    notify_me(notify_title, notify_text) #Calling the function...
